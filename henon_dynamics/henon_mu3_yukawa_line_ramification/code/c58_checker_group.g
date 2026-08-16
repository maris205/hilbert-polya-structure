# Independent finite-group reconstruction for the HCS-C58 checker.
#
# This file intentionally contains its own W(E6) permutation and Picard
# representations.  It does not read producer output or producer source.  Its
# only output is one canonical JSON line, consumed by c58_checker.py.

if LoadPackage("tomlib") <> true then
  Error("the GAP tomlib package is required");
fi;
if LoadPackage("ctbllib") <> true then
  Error("the GAP ctbllib package is required");
fi;
SizeScreen([1000000,1000000]);;

W27gens := [
  (1,2)(8,12)(9,13)(10,14)(11,15)(22,23),
  (2,3)(7,8)(13,16)(14,17)(15,18)(23,24),
  (3,4)(8,9)(12,13)(17,19)(18,20)(24,25),
  (4,5)(9,10)(13,14)(16,17)(20,21)(25,26),
  (5,6)(10,11)(14,15)(17,18)(19,20)(26,27),
  (1,12)(2,8)(3,7)(19,27)(20,26)(21,25)
];;
W27 := Group(W27gens);;

W36gens := [
  (6,17)(7,18)(8,19)(9,20)(10,21)(11,22)(13,23)(14,24)(15,25)(16,26),
  (3,6)(4,7)(5,8)(12,13)(20,27)(21,28)(22,29)(24,30)(25,31)(26,32),
  (2,3)(7,9)(8,10)(13,14)(18,20)(19,21)(23,24)(29,33)(31,34)(32,35),
  (3,4)(6,7)(10,11)(14,15)(17,18)(21,22)(24,25)(28,29)(30,31)(35,36),
  (4,5)(7,8)(9,10)(15,16)(18,19)(20,21)(25,26)(27,28)(31,32)(34,35),
  (1,33)(3,30)(4,31)(5,32)(6,24)(7,25)(8,26)(14,17)(15,18)(16,19)
];;
W36 := Group(W36gens);;
phi36 := GroupHomomorphismByImages(W27,W36,W27gens,W36gens);;

M7gens := [
  [[1,0,0,0,0,0,0],[0,0,1,0,0,0,0],[0,1,0,0,0,0,0],[0,0,0,1,0,0,0],[0,0,0,0,1,0,0],[0,0,0,0,0,1,0],[0,0,0,0,0,0,1]],
  [[1,0,0,0,0,0,0],[0,1,0,0,0,0,0],[0,0,0,1,0,0,0],[0,0,1,0,0,0,0],[0,0,0,0,1,0,0],[0,0,0,0,0,1,0],[0,0,0,0,0,0,1]],
  [[1,0,0,0,0,0,0],[0,1,0,0,0,0,0],[0,0,1,0,0,0,0],[0,0,0,0,1,0,0],[0,0,0,1,0,0,0],[0,0,0,0,0,1,0],[0,0,0,0,0,0,1]],
  [[1,0,0,0,0,0,0],[0,1,0,0,0,0,0],[0,0,1,0,0,0,0],[0,0,0,1,0,0,0],[0,0,0,0,0,1,0],[0,0,0,0,1,0,0],[0,0,0,0,0,0,1]],
  [[1,0,0,0,0,0,0],[0,1,0,0,0,0,0],[0,0,1,0,0,0,0],[0,0,0,1,0,0,0],[0,0,0,0,1,0,0],[0,0,0,0,0,0,1],[0,0,0,0,0,1,0]],
  [[2,1,1,1,0,0,0],[-1,0,-1,-1,0,0,0],[-1,-1,0,-1,0,0,0],[-1,-1,-1,0,0,0,0],[0,0,0,0,1,0,0],[0,0,0,0,0,1,0],[0,0,0,0,0,0,1]]
];;
M7 := Group(M7gens);;
phi7 := GroupHomomorphismByImages(W27,M7,W27gens,M7gens);;

if Size(W27) <> 51840 or not IsBijective(phi36) or not IsBijective(phi7) then
  Error("the three frozen W(E6) actions did not identify bijectively");
fi;

tom := TableOfMarks("U4(2).2");;
tomGroup := UnderlyingGroup(tom);;
toW := IsomorphismGroups(tomGroup,W27);;
if toW = fail or not IsBijective(toW) then
  Error("tomlib U4(2).2 did not identify with the frozen W(E6)");
fi;
tomOrders := OrdersTom(tom);;

TomImage := function(index)
  return Image(toW,RepresentativeTom(tom,index));
end;;

OrbitSizes := function(group,degree)
  return SortedList(List(Orbits(group,[1..degree]),Length));
end;;

FixDims := function(group)
  local image7,v6,permutation,v20;
  image7 := Image(phi7,group);
  v6 := Sum(Elements(image7),TraceMat)/Size(image7)-1;
  permutation := Length(Orbits(group,[1..27]));
  v20 := permutation-1-v6;
  if not IsInt(v6) or not IsInt(v20) then
    Error("nonintegral fixed-space dimension");
  fi;
  return [v6,v20];
end;;

RefinementCodims := function(big,small)
  local blocks,out,block;
  blocks := ShallowCopy(Orbits(big,[1..27]));
  Sort(blocks,function(left,right) return Length(left)<Length(right); end);
  out := [];
  for block in blocks do
    Add(out,Length(block)-Length(Orbits(small,block)));
  od;
  return out;
end;;

OrbitRunLength := function(values)
  local sorted,result,value;
  sorted := ShallowCopy(values);;
  Sort(sorted);
  result := [];;
  for value in sorted do
    if Length(result)>0 and result[Length(result)][1]=value then
      result[Length(result)][2] := result[Length(result)][2]+1;
    else
      Add(result,[value,1]);
    fi;
  od;
  return result;
end;;

RationalPairs := function(values)
  return List(values,value -> [NumeratorRat(value),DenominatorRat(value)]);
end;;

ScaledRefinementContributions := function(inertia,layer)
  local denominator;
  denominator := Size(inertia)/Size(layer);;
  return List(RefinementCodims(inertia,layer),value -> value/denominator);
end;;

TwoLayerSolutions := function(base,wildContribution,deepContribution,target)
  local rhs,formal,found,left,right,determinant,wildLayers,deepLayers,
        solutions;
  rhs := List([1..Length(base)],index -> target[index]-base[index]);;
  formal := fail;;
  found := false;;
  for left in [1..Length(base)-1] do
    for right in [left+1..Length(base)] do
      determinant := wildContribution[left]*deepContribution[right]
        - wildContribution[right]*deepContribution[left];;
      if determinant<>0 and not found then
        wildLayers := (rhs[left]*deepContribution[right]
          - rhs[right]*deepContribution[left])/determinant;;
        deepLayers := (wildContribution[left]*rhs[right]
          - wildContribution[right]*rhs[left])/determinant;;
        if ForAll([1..Length(base)],index ->
          base[index]+wildLayers*wildContribution[index]
            +deepLayers*deepContribution[index]=target[index]) then
          formal := [wildLayers,deepLayers];;
          found := true;;
        fi;
      fi;
    od;
  od;
  if formal=fail or not ForAll(formal,IsInt) then
    Error("p=3 deep-C3 filtration system lacks an integral formal solution");
  fi;
  solutions := [];;
  if ForAll(formal,value -> value>=0) then
    Add(solutions,formal);
  fi;
  return rec(formal_integer_solution := formal,
    nonnegative_integer_solutions := solutions);
end;;

DualHitsAllOrders := function(target27,target36)
  local result,index,group;
  result := [];
  for index in [1..Length(tomOrders)] do
    group := TomImage(index);
    if OrbitSizes(group,27)=target27 and
       OrbitSizes(Image(phi36,group),36)=target36 then
      Add(result,[index,group]);
    fi;
  od;
  return result;
end;;

p3target27 := [3,6,9,9];;
p3target36 := [3,3,3,9,18];;
p3baseDifferent := [2,5,8,8];;
p3targetDifferent := [3,7,18,18];;

TomIndexOfSubgroup := function(subgroup)
  local index;
  for index in [1..Length(tomOrders)] do
    if tomOrders[index]=Size(subgroup) and
       IsConjugate(W27,subgroup,TomImage(index)) then
      return index;
    fi;
  od;
  Error("subgroup was not found in the table of marks");
end;;

p3hits := DualHitsAllOrders(p3target27,p3target36);;
p3allhits := [];;
for pair in p3hits do
  group := pair[2];;
  wild := SylowSubgroup(group,3);;
  if not IsNormal(group,wild) then
    Error("p=3 dual-pattern hit has nonnormal wild Sylow subgroup");
  fi;
  tameQuotient := FactorGroup(group,wild);;
  Add(p3allhits,rec(
    decomposition_orbits_27 := OrbitSizes(group,27),
    decomposition_orbits_36 := OrbitSizes(Image(phi36,group),36),
    id_group := IdGroup(group),
    order := Size(group),
    tame_quotient_cyclic := IsCyclic(tameQuotient),
    tame_quotient_id_group := IdGroup(tameQuotient),
    tom_index := pair[1],
    wild_sylow_3_id_group := IdGroup(wild),
    wild_sylow_3_normal := true
  ));
od;
p3pairrecords := [];;
p3inertiahits := [];;
for pair in p3hits do
  decompositionIndex := pair[1];;
  decomposition := pair[2];;
  for subgroupClass in ConjugacyClassesSubgroups(decomposition) do
    inertia := Representative(subgroupClass);;
    if IsNormal(decomposition,inertia) and
       OrbitSizes(inertia,27)=p3target27 and
       IsCyclic(FactorGroup(decomposition,inertia)) then
      wild := SylowSubgroup(inertia,3);;
      if IsNormal(decomposition,wild) and IsNormal(inertia,wild) and
         IsCyclic(FactorGroup(inertia,wild)) then
        deepEntries := [];;
        for deepClass in ConjugacyClassesSubgroups(wild) do
          deep := Representative(deepClass);;
          if Size(deep)=3 then
            deepIndex := TomIndexOfSubgroup(deep);;
            normalInInertia := IsNormal(inertia,deep);;
            normalInDecomposition := IsNormal(decomposition,deep);;
            if not normalInInertia then
              tameAction := "NOT_INERTIA_NORMAL";;
            elif IsSubgroup(Centre(inertia),deep) then
              tameAction := "central";;
            else
              tameAction := "inversion";;
            fi;
            Add(deepEntries,rec(
              normal_in_decomposition := normalInDecomposition,
              normal_in_inertia := normalInInertia,
              tame_action := tameAction,
              tom_index := deepIndex
            ));
          fi;
        od;
        if Length(deepEntries)<>4 then
          Error("p=3 pair did not enumerate all four C3 subgroups of C3^2");
        fi;
        deepProfileSummary := [];;
        for deepIndex in SortedList(Set(List(deepEntries,row -> row.tom_index))) do
          selectedDeepEntries := Filtered(deepEntries,
            row -> row.tom_index=deepIndex);;
          Add(deepProfileSummary,rec(
            central_action_multiplicity := Number(selectedDeepEntries,
              row -> row.tame_action="central"),
            inversion_action_multiplicity := Number(selectedDeepEntries,
              row -> row.tame_action="inversion"),
            multiplicity := Length(selectedDeepEntries),
            normal_in_decomposition_multiplicity := Number(selectedDeepEntries,
              row -> row.normal_in_decomposition),
            normal_in_inertia_multiplicity := Number(selectedDeepEntries,
              row -> row.normal_in_inertia),
            not_inertia_normal_multiplicity := Number(selectedDeepEntries,
              row -> row.tame_action="NOT_INERTIA_NORMAL"),
            tom_index := deepIndex
          ));
        od;
        inertiaIndex := TomIndexOfSubgroup(inertia);;
        Add(p3pairrecords,rec(
          deep_C3_profile_summary := deepProfileSummary,
          deep_C3_subgroup_count := Length(deepEntries),
          decomposition_tom_index := decompositionIndex,
          inertia_tom_index := inertiaIndex,
          residue_quotient_order := Size(decomposition)/Size(inertia)
        ));
        if Position(List(p3inertiahits,row -> row[1]),inertiaIndex)=fail then
          Add(p3inertiahits,[inertiaIndex,inertia]);
        fi;
      fi;
    fi;
  od;
od;
Sort(p3pairrecords,function(left,right)
  if left.decomposition_tom_index<>right.decomposition_tom_index then
    return left.decomposition_tom_index<right.decomposition_tom_index;
  fi;
  return left.inertia_tom_index<right.inertia_tom_index;
end);

# Pre-bind loop-state globals so GAP's parser does not emit unbound-global
# warnings for the immediately evaluated filter closures below.
deepRows := [];;
deepProfiles := [];;
firstDeepRow := fail;;
selectedDeepIndex := 0;;
p3records := [];;
for pair in p3inertiahits do
  index := pair[1];;
  inertia := pair[2];;
  wild := SylowSubgroup(inertia,3);;
  wildContribution := ScaledRefinementContributions(inertia,wild);;
  deepGroups := [];;
  deepRows := [];;
  for subgroupClass in ConjugacyClassesSubgroups(wild) do
    deep := Representative(subgroupClass);
    if Size(deep)=3 then
      deepIndex := TomIndexOfSubgroup(deep);;
      deepContribution := ScaledRefinementContributions(inertia,deep);;
      layerSolutions := TwoLayerSolutions(p3baseDifferent,wildContribution,
        deepContribution,p3targetDifferent);;
      if not IsNormal(inertia,deep) then
        tameAction := "NOT_INERTIA_NORMAL";;
      elif IsSubgroup(Centre(inertia),deep) then
        tameAction := "central";;
      else
        tameAction := "inversion";;
      fi;
      Add(deepGroups,deep);;
      Add(deepRows,rec(
        double_six_orbit_rle := OrbitRunLength(
          OrbitSizes(Image(phi36,deep),36)),
        fixed_dimensions_V6_V20 := FixDims(deep),
        formal_integer_solution := layerSolutions.formal_integer_solution,
        line_orbit_rle := OrbitRunLength(OrbitSizes(deep,27)),
        nonnegative_integer_solutions :=
          layerSolutions.nonnegative_integer_solutions,
        normal_in_inertia := IsNormal(inertia,deep),
        per_layer_different_contribution_num_den :=
          RationalPairs(deepContribution),
        tame_action := tameAction,
        tom_index := deepIndex
      ));
    fi;
  od;
  if Length(deepRows)<>4 then
    Error("p=3 inertia did not enumerate all four C3 subgroups of C3^2");
  fi;
  deepProfiles := [];;
  for deepIndex in SortedList(Set(List(deepRows,row -> row.tom_index))) do
    matchingPositions := Filtered([1..Length(deepRows)],
      position -> deepRows[position].tom_index=deepIndex);;
    firstDeepRow := deepRows[matchingPositions[1]];;
    if not ForAll(matchingPositions,position ->
      deepRows[position].double_six_orbit_rle=firstDeepRow.double_six_orbit_rle and
      deepRows[position].fixed_dimensions_V6_V20=firstDeepRow.fixed_dimensions_V6_V20 and
      deepRows[position].formal_integer_solution=firstDeepRow.formal_integer_solution and
      deepRows[position].line_orbit_rle=firstDeepRow.line_orbit_rle and
      deepRows[position].nonnegative_integer_solutions=firstDeepRow.nonnegative_integer_solutions and
      deepRows[position].per_layer_different_contribution_num_den=
        firstDeepRow.per_layer_different_contribution_num_den) then
      Error("one ToM deep-C3 profile has inconsistent arithmetic carriers");
    fi;
    Add(deepProfiles,rec(
      double_six_orbit_rle := firstDeepRow.double_six_orbit_rle,
      fixed_dimensions_V6_V20 := firstDeepRow.fixed_dimensions_V6_V20,
      formal_integer_solution := firstDeepRow.formal_integer_solution,
      line_orbit_rle := firstDeepRow.line_orbit_rle,
      multiplicity := Length(matchingPositions),
      nonnegative_integer_solutions :=
        firstDeepRow.nonnegative_integer_solutions,
      per_layer_different_contribution_num_den :=
        firstDeepRow.per_layer_different_contribution_num_den,
      tom_index := deepIndex
    ));
  od;
  selectedProfilePositions := Filtered([1..Length(deepProfiles)],position ->
    deepProfiles[position].nonnegative_integer_solutions<>[]);;
  if Length(selectedProfilePositions)<>1 then
    Error("p=3 different equations did not select exactly one deep-C3 profile");
  fi;
  selectedDeepIndex := deepProfiles[selectedProfilePositions[1]].tom_index;;
  selectedDeepPositions := Filtered([1..Length(deepRows)],position ->
    deepRows[position].tom_index=selectedDeepIndex and
    deepRows[position].normal_in_inertia);;
  if Length(selectedDeepPositions)<>1 then
    Error("selected p=3 deep-C3 profile is not uniquely inertia-normal");
  fi;
  deep := deepGroups[selectedDeepPositions[1]];;
  selectedDeepRow := deepRows[selectedDeepPositions[1]];;
  Add(p3records,rec(
    central_deep_c3 := IsSubgroup(Centre(inertia),deep),
    core_order := Size(Core(W27,inertia)),
    deep_C3_profiles := deepProfiles,
    deep_id_group := IdGroup(deep),
    deep_orbits_27 := OrbitSizes(deep,27),
    deep_orbits_36 := OrbitSizes(Image(phi36,deep),36),
    fixed_dimensions_deep := FixDims(deep),
    fixed_dimensions_inertia := FixDims(inertia),
    fixed_dimensions_wild := FixDims(wild),
    inertia_id_group := IdGroup(inertia),
    inertia_orbits_27 := OrbitSizes(inertia,27),
    inertia_orbits_36 := OrbitSizes(Image(phi36,inertia),36),
    normalizer_order := Size(Normalizer(W27,inertia)),
    refinement_codimensions_deep := RefinementCodims(inertia,deep),
    refinement_codimensions_wild := RefinementCodims(inertia,wild),
    selected_deep_tame_action := selectedDeepRow.tame_action,
    selected_deep_tom_index := selectedDeepIndex,
    tom_index := index,
    wild_id_group := IdGroup(wild),
    wild_orbits_27 := OrbitSizes(wild,27),
    wild_orbits_36 := OrbitSizes(Image(phi36,wild),36)
  ));
od;

if Length(p3records)<>2 or
   p3records[1].deep_C3_profiles<>p3records[2].deep_C3_profiles then
  Error("p=3 inertia candidates disagree on exhaustive deep-C3 profiles");
fi;
p3SelectedDeepProfiles := Filtered(p3records[1].deep_C3_profiles,
  row -> row.nonnegative_integer_solutions<>[]);;
if Length(p3SelectedDeepProfiles)<>1 then
  Error("p=3 deep-C3 profile selection is not unique");
fi;
p3DeepActionByInertia := List(p3records,row -> rec(
  inertia_tom_index := row.tom_index,
  tame_action := row.selected_deep_tame_action
));;
p3DeepExhaustion := rec(
  base_different_vector_num_den := RationalPairs(p3baseDifferent),
  profiles := p3records[1].deep_C3_profiles,
  selected_tom_index := p3SelectedDeepProfiles[1].tom_index,
  solution_variable_order := ["wild_C3_squared_layers","deep_C3_layers"],
  target_different_vector_num_den := RationalPairs(p3targetDifferent),
  wild_C3_squared_per_layer_contribution_num_den :=
    RationalPairs(ScaledRefinementContributions(
      TomImage(p3records[1].tom_index),
      SylowSubgroup(TomImage(p3records[1].tom_index),3)))
);;

p3decomposition := [];;
for pair in p3hits do
  index := pair[1];;
  decomposition := pair[2];;
  contained := [];;
  for pairRecord in p3pairrecords do
    if pairRecord.decomposition_tom_index=index then
      Add(contained,rec(
        inertia_tom_index := pairRecord.inertia_tom_index,
        residue_quotient_order := pairRecord.residue_quotient_order
      ));
    fi;
  od;
  Add(p3decomposition,rec(
    contained_inertia := contained,
    id_group := IdGroup(decomposition),
    normalizer_order := Size(Normalizer(W27,decomposition)),
    tom_index := index
  ));
od;

p5target27 := [1,1,5,5,5,10];;
p5target36 := [1,5,10,10,10];;
p5hits := DualHitsAllOrders(p5target27,p5target36);;
p5allhits := [];;
for pair in p5hits do
  index := pair[1];;
  inertia := pair[2];;
  wild := SylowSubgroup(inertia,5);;
  Add(p5allhits,rec(
    decomposition_orbits_27 := OrbitSizes(inertia,27),
    decomposition_orbits_36 := OrbitSizes(Image(phi36,inertia),36),
    id_group := IdGroup(inertia),
    order := Size(inertia),
    sylow_5_normal := IsNormal(inertia,wild),
    sylow_5_normalizer_order := Size(Normalizer(W27,wild)),
    tom_index := index
  ));
od;
p5pairrecords := [];;
p5inertiahits := [];;
for pair in p5hits do
  decompositionIndex := pair[1];;
  decomposition := pair[2];;
  for subgroupClass in ConjugacyClassesSubgroups(decomposition) do
    inertia := Representative(subgroupClass);;
    if IsNormal(decomposition,inertia) and
       OrbitSizes(inertia,27)=p5target27 and
       IsCyclic(FactorGroup(decomposition,inertia)) then
      wild := SylowSubgroup(inertia,5);;
      if IsNormal(decomposition,wild) and IsNormal(inertia,wild) and
         IsCyclic(FactorGroup(inertia,wild)) then
        inertiaIndex := TomIndexOfSubgroup(inertia);;
        Add(p5pairrecords,rec(
          decomposition_tom_index := decompositionIndex,
          inertia_tom_index := inertiaIndex,
          residue_quotient_order := Size(decomposition)/Size(inertia)
        ));
        if Position(List(p5inertiahits,row -> row[1]),inertiaIndex)=fail then
          Add(p5inertiahits,[inertiaIndex,inertia]);
        fi;
      fi;
    fi;
  od;
od;

p5records := [];;
for pair in p5inertiahits do
    index := pair[1];;
    inertia := pair[2];;
    wild := SylowSubgroup(inertia,5);;
    Add(p5records,rec(
      fixed_dimensions_inertia := FixDims(inertia),
      fixed_dimensions_wild := FixDims(wild),
      inertia_id_group := IdGroup(inertia),
      inertia_orbits_27 := OrbitSizes(inertia,27),
      inertia_orbits_36 := OrbitSizes(Image(phi36,inertia),36),
      normalizer_order := Size(Normalizer(W27,inertia)),
      refinement_codimensions_wild := RefinementCodims(inertia,wild),
      tom_index := index,
      wild_central := IsSubgroup(Centre(inertia),wild),
      wild_id_group := IdGroup(wild),
      wild_normal := IsNormal(inertia,wild),
      wild_normalizer_order := Size(Normalizer(W27,wild)),
      wild_orbits_27 := OrbitSizes(wild,27),
      wild_orbits_36 := OrbitSizes(Image(phi36,wild),36)
    ));
od;

order3records := [];;
for index in [1..Length(tomOrders)] do
  if tomOrders[index]=3 then
    group := TomImage(index);
    Add(order3records,rec(
      fixed_dimensions := FixDims(group),
      normalizer_order := Size(Normalizer(W27,group)),
      orbits_27 := OrbitSizes(group,27),
      orbits_36 := OrbitSizes(Image(phi36,group),36),
      tom_index := index
    ));
  fi;
od;

order2records := [];;
for index in [1..Length(tomOrders)] do
  if tomOrders[index]=2 then
    group := TomImage(index);
    Add(order2records,rec(
      fixed_dimensions := FixDims(group),
      normalizer_order := Size(Normalizer(W27,group)),
      orbits_27 := OrbitSizes(group,27),
      orbits_36 := OrbitSizes(Image(phi36,group),36),
      tom_index := index
    ));
  fi;
od;

# Derive the character-table class attached to every order-two ToM class.
# A cyclic subgroup of order two has trivial automorphism group, so its
# normalizer is the centralizer of its nonidentity element.  Consequently its
# subgroup-class size is also the element-class size.  Matching order and this
# class size inside CharacterTable("U4(2).2") is unique in all four cases; in
# particular the geometry-selected ToM class 5 will map to element class 17
# without either index being supplied as an input to this computation.
characterTable := CharacterTable("U4(2).2");;
characterOrders := OrdersClassRepresentatives(characterTable);;
characterSizes := SizesConjugacyClasses(characterTable);;
order2CharacterTableMap := [];;
for record in order2records do
  subgroup := TomImage(record.tom_index);;
  involution := First(Elements(subgroup),element -> Order(element)=2);;
  centralizerOrder := Size(Centralizer(W27,involution));;
  classSize := Size(W27)/centralizerOrder;;
  matchingIndices := [];;
  for candidateIndex in [1..NrConjugacyClasses(characterTable)] do
    if characterOrders[candidateIndex]=2 and
       characterSizes[candidateIndex]=classSize then
      Add(matchingIndices,candidateIndex);
    fi;
  od;
  if Size(characterTable)<>Size(W27) or
     Size(subgroup)<>2 or
     centralizerOrder<>record.normalizer_order or
     Length(matchingIndices)<>1 then
    Error("order-two ToM/character-table mapping is not unique");
  fi;
  classIndex := matchingIndices[1];;
  Add(order2CharacterTableMap,rec(
    character_table_group_order := Size(characterTable),
    character_table_name := "U4(2).2",
    element_centralizer_order := Size(characterTable)/characterSizes[classIndex],
    element_class_index := classIndex,
    element_class_matching_indices := matchingIndices,
    element_class_order := characterOrders[classIndex],
    element_class_size := characterSizes[classIndex],
    subgroup_generator_centralizer_order := centralizerOrder,
    subgroup_normalizer_order := record.normalizer_order,
    subgroup_order := Size(subgroup),
    subgroup_tom_index := record.tom_index,
    unique_order_and_class_size_match := true
  ));
od;

# At the three tame C3 primes the degree-27 field alone leaves two C3
# conjugacy classes.  The frozen degree-36 resolvers supply decomposition
# orbit degrees, not inertia orbit degrees.  Exhaust all pairs I normal in D
# with cyclic residue quotient and compare both labelled actions.
tamePairRecords := [];;
for index in [1..Length(tomOrders)] do
  decomposition := TomImage(index);
  if OrbitSizes(decomposition,27)=[3,6,18] and
     OrbitSizes(Image(phi36,decomposition),36)=[3,6,9,18] then
    for subgroupClass in ConjugacyClassesSubgroups(decomposition) do
      inertia := Representative(subgroupClass);
      if Size(inertia)=3 and IsNormal(decomposition,inertia) and
         IsCyclic(FactorGroup(decomposition,inertia)) and
         OrbitSizes(inertia,27)=[3,3,3,3,3,3,3,3,3] then
        inertiaTom := fail;;
        for inertiaIndex in [1..Length(tomOrders)] do
          if tomOrders[inertiaIndex]=3 and
             IsConjugate(W27,inertia,TomImage(inertiaIndex)) then
            inertiaTom := inertiaIndex;
            break;
          fi;
        od;
        if inertiaTom=fail then Error("tame C3 class not found in table of marks"); fi;
        Add(tamePairRecords,rec(
          decomposition_id_group := IdGroup(decomposition),
          decomposition_orbits_27 := OrbitSizes(decomposition,27),
          decomposition_orbits_36 := OrbitSizes(Image(phi36,decomposition),36),
          decomposition_order := Size(decomposition),
          decomposition_tom_index := index,
          inertia_fixed_dimensions := FixDims(inertia),
          inertia_orbits_27 := OrbitSizes(inertia,27),
          inertia_orbits_36 := OrbitSizes(Image(phi36,inertia),36),
          inertia_tom_index := inertiaTom,
          quotient_order := Size(decomposition)/3
        ));
      fi;
    od;
  fi;
od;

# Restricted JSON encoder: the report contains only records, lists, safe ASCII
# strings, integers and booleans.  Record names are sorted recursively, making
# the single output line byte-canonical for the Python side.
JsonValue := function(value)
  local names,pieces,name;
  if IsList(value) and Length(value)=0 then
    return "[]";
  elif IsString(value) then
    if PositionSublist(value,"\\")<>fail or PositionSublist(value,"\"")<>fail then
      Error("unsafe string in JSON report");
    fi;
    return Concatenation("\"",value,"\"");
  elif IsBool(value) then
    if value then return "true"; else return "false"; fi;
  elif IsInt(value) then
    return String(value);
  elif IsList(value) then
    return Concatenation("[",JoinStringsWithSeparator(List(value,JsonValue),","),"]");
  elif IsRecord(value) then
    names := SortedList(RecNames(value));
    pieces := [];
    for name in names do
      Add(pieces,Concatenation("\"",name,"\":",JsonValue(value.(name))));
    od;
    return Concatenation("{",JoinStringsWithSeparator(pieces,","),"}");
  fi;
  Error("unsupported value in JSON report");
end;;

report := rec(
  action_generators := rec(
    double_six_point_images := List(W36gens,
      generator -> List([1..36],point -> point^generator)),
    line_point_images := List(W27gens,
      generator -> List([1..27],point -> point^generator)),
    picard_matrices := M7gens
  ),
  actions := rec(
    double_six_action_bijective := IsBijective(phi36),
    double_six_degree := 36,
    line_degree := 27,
    picard_action_bijective := IsBijective(phi7),
    picard_lattice_rank := 7,
    weyl_group_order := Size(W27)
  ),
  order2_classes := order2records,
  order2_character_table_map := order2CharacterTableMap,
  order3_classes := order3records,
  p3_filter := rec(
    all_tom_decomposition_pattern_hits := p3allhits,
    deep_C3_exhaustion := p3DeepExhaustion,
    deep_C3_selected_action_by_inertia := p3DeepActionByInertia,
    decomposition_candidates := p3decomposition,
    inertia_candidates := p3records,
    valid_decomposition_inertia_pairs := p3pairrecords
  ),
  p5_filter := rec(
    all_tom_decomposition_pattern_hits := p5allhits,
    inertia_candidates := p5records,
    valid_decomposition_inertia_pairs := p5pairrecords
  ),
  tame_c3_dual_filter := tamePairRecords,
  schema_id := "hcs-c58-checker-group-report-v1"
);;

stdout := OutputTextUser();;
SetPrintFormattingStatus(stdout,false);;
PrintTo(stdout,JsonValue(report),"\n");
QUIT;
