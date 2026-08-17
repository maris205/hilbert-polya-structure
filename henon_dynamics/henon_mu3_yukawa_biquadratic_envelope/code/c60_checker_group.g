# Independent GAP reconstruction for the staged C60 normalizer-tower lane.
#
# Every distinguished subgroup is defined by a durable one-based permutation
# array on the released 27-line carrier.  TomLib independently locates those
# groups, exhausts all 350 transitive permutation characters and scans all
# eleven collision buckets.  The checker emits compact canonical JSON only.

if GAPInfo.Version <> "4.11.1" then
  Error("frozen GAP version changed");
fi;
if LoadPackage("tomlib") <> true then Error("TomLib is required"); fi;
if LoadPackage("ctbllib") <> true then Error("CTblLib is required"); fi;
if LoadPackage("smallgrp") <> true then Error("SmallGrp is required"); fi;
if PackageInfo("TomLib")[1].Version <> "1.2.9" then
  Error("frozen TomLib version changed");
fi;
if PackageInfo("CTblLib")[1].Version <> "1.3.1" then
  Error("frozen CTblLib version changed");
fi;
if PackageInfo("SmallGrp")[1].Version <> "1.4.1" then
  Error("frozen SmallGrp version changed");
fi;
SizeScreen([1000000,1000000]);;

AssertEqual := function(label, got, expected)
  if got <> expected then
    Error(Concatenation(label, " changed: got ", String(got),
      ", expected ", String(expected)));
  fi;
end;;

W27Arrays := [
  [2,1,3,4,5,6,7,12,13,14,15,8,9,10,11,16,17,18,19,20,21,23,22,24,25,26,27],
  [1,3,2,4,5,6,8,7,9,10,11,12,16,17,18,13,14,15,19,20,21,22,24,23,25,26,27],
  [1,2,4,3,5,6,7,9,8,10,11,13,12,14,15,16,19,20,17,18,21,22,23,25,24,26,27],
  [1,2,3,5,4,6,7,8,10,9,11,12,14,13,15,17,16,18,19,21,20,22,23,24,26,25,27],
  [1,2,3,4,6,5,7,8,9,11,10,12,13,15,14,16,18,17,20,19,21,22,23,24,25,27,26],
  [12,8,7,4,5,6,3,2,9,10,11,1,13,14,15,16,17,18,27,26,25,22,23,24,21,20,19]
];;
H301Arrays := [
  [1,2,19,21,20,3,24,11,9,10,23,15,13,14,22,5,4,18,6,16,17,12,8,27,25,26,7],
  [16,27,13,12,22,26,15,25,24,7,14,18,20,5,1,23,8,17,9,19,6,2,10,3,4,21,11],
  [26,13,22,20,24,15,21,3,14,1,19,11,25,18,23,7,5,9,12,27,16,8,6,17,2,10,4]
];;
H303Arrays := [
  [5,1,6,2,3,4,10,21,14,17,19,11,7,8,9,15,18,20,12,13,16,26,22,27,23,24,25],
  [7,15,13,12,26,5,16,18,20,1,22,8,9,6,27,11,4,25,3,24,14,10,21,19,17,23,2],
  [16,23,9,8,26,27,7,25,24,10,11,12,13,6,5,22,17,18,19,20,2,1,21,3,4,15,14]
];;
Branch140DArrays := [
  [7,26,13,12,5,15,1,18,20,22,16,4,3,14,6,11,25,8,24,9,27,10,23,19,17,2,21],
  [17,2,21,4,18,1,15,5,20,3,11,12,22,14,25,16,6,8,19,23,10,27,9,24,7,26,13],
  [23,24,22,19,21,20,1,3,15,13,14,2,18,16,17,11,9,10,26,25,27,8,7,12,6,4,5]
];;
Branch140PArrays := [
  [7,12,8,26,27,25,23,22,17,18,16,24,10,11,9,14,15,13,4,6,5,3,1,2,20,19,21],
  [25,12,18,26,22,15,20,13,1,5,16,24,21,11,23,14,7,27,4,17,8,10,6,2,9,19,3]
];;
Branch140QArrays := [
  [6,2,10,4,8,17,25,18,23,21,11,12,27,14,7,16,1,5,19,9,3,13,20,24,15,26,22]
];;
Branch206DArrays := [
  [1,2,20,16,5,18,26,8,11,23,9,12,15,22,13,4,17,6,21,3,19,14,10,24,27,7,25],
  [5,2,3,4,1,6,14,17,19,10,21,12,13,7,15,16,8,18,9,20,11,26,23,24,25,22,27],
  [11,7,26,24,25,15,22,14,12,13,27,21,18,20,23,4,3,10,5,8,9,2,6,16,19,17,1]
];;
Branch206IArrays := [
  [1,17,22,16,12,18,26,8,25,23,27,5,15,20,13,4,2,6,21,14,19,3,10,24,9,7,11],
  [11,7,26,24,25,15,22,14,12,13,27,21,18,20,23,4,3,10,5,8,9,2,6,16,19,17,1],
  [12,17,14,4,1,6,3,2,19,10,21,5,13,7,15,16,8,18,27,22,25,26,23,24,11,20,9]
];;
Branch206PArrays := [
  [11,7,26,24,25,15,22,14,12,13,27,21,18,20,23,4,3,10,5,8,9,2,6,16,19,17,1],
  [12,17,14,4,1,6,3,2,19,10,21,5,13,7,15,16,8,18,27,22,25,26,23,24,11,20,9]
];;
Branch206QArrays := [
  [12,17,14,4,1,6,3,2,19,10,21,5,13,7,15,16,8,18,27,22,25,26,23,24,11,20,9]
];;

# Frozen C60 successor arrays.  These are data, not discoveries at replay
# time: the dynamic normalizer/TomLib reconstruction below must recover them.
N301Arrays := [
  [1,18,22,16,17,12,27,8,25,26,23,6,14,13,19,4,5,2,15,21,20,3,11,24,9,10,7],
  [15,12,4,14,25,7,10,27,8,6,17,24,11,3,21,26,13,22,5,18,1,20,16,2,19,23,9],
  [1,2,19,21,20,3,24,11,9,10,23,15,13,14,22,5,4,18,6,16,17,12,8,27,25,26,7],
  [14,10,3,7,4,6,5,8,2,9,11,12,1,13,15,17,27,25,19,21,24,22,23,20,26,18,16],
  [18,1,15,4,5,12,7,6,13,14,3,8,26,25,11,16,17,2,22,20,21,23,19,24,10,9,27],
  [1,13,16,12,6,5,8,7,9,26,27,4,2,18,17,3,15,14,20,19,22,21,24,23,25,10,11]
];;
H302Arrays := [
  [2,18,23,21,20,11,24,15,26,25,22,3,9,10,19,5,4,1,8,16,17,6,12,27,14,13,7],
  [13,9,6,16,27,19,17,23,10,2,8,22,14,1,12,24,20,26,3,7,5,15,11,4,18,25,21],
  [15,12,4,14,25,7,10,27,8,6,17,24,11,3,21,26,13,22,5,18,1,20,16,2,19,23,9],
  [1,2,19,21,20,3,24,11,9,10,23,15,13,14,22,5,4,18,6,16,17,12,8,27,25,26,7],
  [20,5,3,2,9,11,10,8,7,4,6,23,24,21,19,26,18,16,15,13,1,22,12,14,17,27,25]
];;
JArrays := [
  [1,2,6,17,16,19,27,23,9,10,8,22,13,14,12,20,21,18,3,5,4,15,11,7,25,26,24],
  [2,18,11,4,5,8,7,12,26,25,15,6,9,10,3,16,17,1,23,20,21,19,22,24,14,13,27],
  [3,6,5,2,1,4,18,17,12,8,16,21,15,11,20,14,10,19,7,13,9,24,27,26,23,22,25]
];;
NormalizerConjugatorArray :=
  [1,15,14,13,22,12,27,26,25,7,24,16,17,6,19,18,5,20,4,21,3,2,11,10,9,23,8];;

W27gens := List(W27Arrays, PermList);;
W27 := Group(W27gens);;
H301 := Group(List(H301Arrays, PermList));;
H303 := Group(List(H303Arrays, PermList));;
D140 := Group(List(Branch140DArrays, PermList));;
I140 := D140;;
P140 := Group(List(Branch140PArrays, PermList));;
Q140 := Group(List(Branch140QArrays, PermList));;
D206 := Group(List(Branch206DArrays, PermList));;
I206 := Group(List(Branch206IArrays, PermList));;
P206 := Group(List(Branch206PArrays, PermList));;
Q206 := Group(List(Branch206QArrays, PermList));;

AssertEqual("W(E6) order", Size(W27), 51840);
AssertEqual("H301 order", Size(H301), 162);
AssertEqual("H303 order", Size(H303), 162);

tom := TableOfMarks("U4(2).2");;
tomGroup := UnderlyingGroup(tom);;
toW := IsomorphismGroups(tomGroup, W27);;
if toW = fail or not IsBijective(toW) then
  Error("TomLib U4(2).2 failed to locate the frozen W(E6) carrier");
fi;
tomOrders := OrdersTom(tom);;
ct := CharacterTable("U4(2).2");;
permutationCharacters := PermCharsTom(ct, tom);;

TomImage := function(index)
  return Image(toW, RepresentativeTom(tom,index));
end;;
TomIndexOfFrozen := function(subgroup)
  local index;
  for index in [1..Length(tomOrders)] do
    if tomOrders[index] = Size(subgroup) and
       IsConjugate(W27, subgroup, TomImage(index)) then
      return index;
    fi;
  od;
  Error("frozen subgroup absent from TableOfMarks(U4(2).2)");
end;;

AssertEqual("ToM class count", Length(tomOrders), 350);
AssertEqual("H301 ToM locator", TomIndexOfFrozen(H301), 301);
AssertEqual("H303 ToM locator", TomIndexOfFrozen(H303), 303);

inventory := [];;
for index in [1..Length(tomOrders)] do
  Add(inventory, rec(
    field_degree := 51840 / tomOrders[index],
    permutation_character_values :=
      List(ValuesOfClassFunction(permutationCharacters[index]), Int),
    subgroup_order := tomOrders[index],
    tom_index := index
  ));
od;

duplicateBuckets := [];;
seen := [];;
for left in [1..Length(permutationCharacters)] do
  if not left in seen then
    rightHits := Filtered([left+1..Length(permutationCharacters)],
      right -> permutationCharacters[right] = permutationCharacters[left]);
    if Length(rightHits) > 0 then
      Add(duplicateBuckets, Concatenation([left],rightHits));
      Append(seen,rightHits);
    fi;
    Add(seen,left);
  fi;
od;
expectedDuplicateBuckets := [
  [12,15],[17,21],[29,36],[31,39],[41,42],[46,48],
  [57,58],[59,64],[112,120],[132,140],[301,303]
];;
AssertEqual("Gassmann collision buckets", duplicateBuckets,
  expectedDuplicateBuckets);
duplicateDegrees := List(duplicateBuckets,
  bucket -> 51840 / tomOrders[bucket[1]]);;
AssertEqual("minimum duplicate degree", Minimum(duplicateDegrees), 320);
AssertEqual("unique degree-320 duplicate bucket count",
  Number(duplicateDegrees, value -> value = 320), 1);
AssertEqual("unique degree-320 duplicate bucket",
  duplicateBuckets[Position(duplicateDegrees,320)], [301,303]);

PairSupport := function(subgroup, seeds)
  local support, seed;
  support := [];
  for seed in seeds do
    UniteSet(support, Set(Orbit(subgroup, Set(seed), OnSets)));
  od;
  return support;
end;;
SupportStabilizer := function(support)
  return Group(Filtered(Elements(W27), element ->
    Set(List(support, pair -> OnSets(pair,element))) = support));
end;;

support301components := List([[1,2],[1,9]], seed ->
  Set(Orbit(H301,Set(seed),OnSets)));;
support303components := List([[1,2]], seed ->
  Set(Orbit(H303,Set(seed),OnSets)));;
support301 := PairSupport(H301, [[1,2],[1,9]]);;
support303 := PairSupport(H303, [[1,2]]);;
stabilizer301 := SupportStabilizer(support301);;
stabilizer303 := SupportStabilizer(support303);;
AssertEqual("H301 support component sizes",
  List(support301components,Length), [27,27]);
AssertEqual("H303 support component sizes",
  List(support303components,Length), [81]);
AssertEqual("H301 support size", Length(support301), 54);
AssertEqual("H303 support size", Length(support303), 81);
AssertEqual("H301 exact support stabilizer", stabilizer301, H301);
AssertEqual("H303 exact support stabilizer", stabilizer303, H303);

FieldReport := function(label, subgroup, tomIndex, supportSeeds,
    supportComponents, support, stabilizer)
  return rec(
    abelian_invariants := AbelianInvariants(subgroup),
    centre_order := Size(Centre(subgroup)),
    core_order := Size(Core(W27,subgroup)),
    derived_subgroup_order := Size(DerivedSubgroup(subgroup)),
    field_degree := Index(W27,subgroup),
    label := label,
    normalizer_order := Size(Normalizer(W27,subgroup)),
    order := Size(subgroup),
    permutation_character_values :=
      List(ValuesOfClassFunction(permutationCharacters[tomIndex]),Int),
    small_group_id := IdGroup(subgroup),
    support := rec(
      component_sizes := List(supportComponents,Length),
      pair_seeds := supportSeeds,
      stabilizer_equals_frozen_field_subgroup := stabilizer = subgroup,
      stabilizer_order := Size(stabilizer),
      support_size := Length(support),
      weyl_orbit_size := Index(W27,stabilizer)
    ),
    tom_locator := tomIndex
  );
end;;

field301 := FieldReport("H301",H301,301,[[1,2],[1,9]],
  support301components,support301,stabilizer301);;
field303 := FieldReport("H303",H303,303,[[1,2]],
  support303components,support303,stabilizer303);;
AssertEqual("H301 SmallGroup", field301.small_group_id, [162,11]);
AssertEqual("H303 SmallGroup", field303.small_group_id, [162,19]);
AssertEqual("H301 abelian invariants", field301.abelian_invariants, [2,3]);
AssertEqual("H303 abelian invariants", field303.abelian_invariants, [2]);
AssertEqual("H301 derived order", field301.derived_subgroup_order, 27);
AssertEqual("H303 derived order", field303.derived_subgroup_order, 81);
AssertEqual("H301 core", field301.core_order, 1);
AssertEqual("H303 core", field303.core_order, 1);
AssertEqual("H301 normalizer", field301.normalizer_order, 324);
AssertEqual("H303 normalizer", field303.normalizer_order, 324);
AssertEqual("H301 centre", field301.centre_order, 1);
AssertEqual("H303 centre", field303.centre_order, 1);
AssertEqual("Gassmann character equality",
  field301.permutation_character_values,
  field303.permutation_character_values);
if IsConjugate(W27,H301,H303) or IdGroup(H301)=IdGroup(H303) then
  Error("frozen field subgroups unexpectedly conjugate or isomorphic");
fi;

AssertBranch := function(label,D,I,P,Q,expectedTom)
  local normal140, normal7;
  AssertEqual(Concatenation(label," orders"),
    List([D,I,P,Q],Size),
    [expectedTom[5],18,9,3]);
  if not IsSubgroup(D,I) or not IsSubgroup(I,P) or not IsSubgroup(P,Q) then
    Error(Concatenation(label," subgroup chain changed"));
  fi;
  if not IsNormal(D,I) or not IsNormal(D,P) or not IsNormal(D,Q) or
     not IsNormal(I,P) or not IsNormal(I,Q) then
    Error(Concatenation(label," filtration normality changed"));
  fi;
  AssertEqual(Concatenation(label," ToM locators"),
    List([D,I,P,Q],TomIndexOfFrozen), expectedTom{[1..4]});
  normal140 := Filtered(List(ConjugacyClassesSubgroups(D),Representative),
    subgroup -> Size(subgroup)=18 and IsNormal(D,subgroup) and
      TomIndexOfFrozen(subgroup)=140);
  AssertEqual(Concatenation(label," normal ToM-140 inertia count"),
    Length(normal140), 1);
  normal7 := Filtered(List(ConjugacyClassesSubgroups(P),Representative),
    subgroup -> Size(subgroup)=3 and IsNormal(I,subgroup) and
      IsNormal(D,subgroup) and TomIndexOfFrozen(subgroup)=7);
  AssertEqual(Concatenation(label," normal ToM-7 deep subgroup count"),
    Length(normal7), 1);
  return rec(
    deep_Q_unique_in_P_subject_to_D_I_normality := true,
    inertia_unique_normal_tom140_in_D := true,
    normality := rec(
      I_normal_in_D := true,
      P_normal_in_D := true,
      P_normal_in_I := true,
      Q_normal_in_D := true,
      Q_normal_in_I := true
    ),
    orders_D_I_P_Q := List([D,I,P,Q],Size),
    tom_D_I_P_Q := List([D,I,P,Q],TomIndexOfFrozen)
  );
end;;

branch140Structure := AssertBranch("D140",D140,I140,P140,Q140,
  [140,140,72,7,18]);;
branch206Structure := AssertBranch("D206",D206,I206,P206,Q206,
  [206,140,72,7,36]);;

i5 := TomImage(147);;
p5 := SylowSubgroup(i5,5);;
tameC3 := TomImage(6);;
reflection := TomImage(2);;
complexConjugation := TomImage(5);;
localSubgroups := [I140,P140,Q140,i5,p5,tameC3,reflection,
  complexConjugation];;
localTomIndices := List(localSubgroups,TomIndexOfFrozen);;
AssertEqual("local subgroup ToM locators",localTomIndices,
  [140,72,7,147,23,6,2,5]);

OrbitCounts := function(field, subgroups)
  local action;
  action := ActionHomomorphism(W27,RightCosets(W27,field),OnRight);
  return List(subgroups, subgroup ->
    Length(Orbits(Image(action,subgroup),[1..Index(W27,field)])));
end;;
counts301 := OrbitCounts(H301,localSubgroups);;
counts303 := OrbitCounts(H303,localSubgroups);;
AssertEqual("H301 local orbit counts",counts301,
  [36,56,112,16,64,128,160,168]);
AssertEqual("H303 local orbit counts",counts303,counts301);
conductors := [
  320-counts301[1]+(320-counts301[2])/2+(320-counts301[3]),
  320-counts301[4]+3*(320-counts301[5])/4,
  320-counts301[6],
  320-counts301[7]
];;
signature := [2*counts301[8]-320,320-counts301[8]];;
AssertEqual("degree-320 conductor exponents",conductors,[624,496,192,160]);
AssertEqual("degree-320 signature",signature,[16,152]);

LocalRows := function(field,D,I,P,Q)
  local action,Dimage,Iimage,Pimage,Qimage,Dorbits,rawRows,orbit,n,f,
        pOrbits,qOrbits,e,conductor,different,collected,degreeTotal,
        differentTotal;
  action := ActionHomomorphism(W27,RightCosets(W27,field),OnRight);
  Dimage := Image(action,D);
  Iimage := Image(action,I);
  Pimage := Image(action,P);
  Qimage := Image(action,Q);
  Dorbits := Orbits(Dimage,[1..Index(W27,field)]);
  rawRows := [];
  for orbit in Dorbits do
    n := Length(orbit);
    f := Length(Orbits(Iimage,orbit));
    pOrbits := Length(Orbits(Pimage,orbit));
    qOrbits := Length(Orbits(Qimage,orbit));
    e := n/f;
    conductor := n-f+(n-pOrbits)/2+(n-qOrbits);
    different := conductor/f;
    if not IsInt(e) or not IsInt(different) or n<>e*f then
      Error("nonintegral or inconsistent complete local row");
    fi;
    Add(rawRows,[n,e,f,different]);
  od;
  Sort(rawRows);
  collected := Collected(rawRows);
  degreeTotal := Sum(collected,row -> row[2]*row[1][1]);
  differentTotal := Sum(collected,
    row -> row[2]*row[1][3]*row[1][4]);
  AssertEqual("complete local degree total",degreeTotal,320);
  AssertEqual("complete local different total",differentTotal,624);
  return rec(
    complete_collected_rows_n_e_f_d_with_multiplicity := collected,
    degree_total := degreeTotal,
    different_exponent_total := differentTotal,
    double_coset_count := Length(Dorbits),
    e_f_identity_all_rows := true
  );
end;;

branch140H301 := LocalRows(H301,D140,I140,P140,Q140);;
branch140H303 := LocalRows(H303,D140,I140,P140,Q140);;
branch206H301 := LocalRows(H301,D206,I206,P206,Q206);;
branch206H303 := LocalRows(H303,D206,I206,P206,Q206);;
AssertEqual("D140/H301 complete rows",
  branch140H301.complete_collected_rows_n_e_f_d_with_multiplicity,
  [[[1,1,1,0],8],[[6,6,1,11],10],[[9,9,1,18],8],[[18,18,1,37],10]]);
AssertEqual("D140/H303 complete rows",
  branch140H303.complete_collected_rows_n_e_f_d_with_multiplicity,
  [[[2,2,1,1],4],[[3,3,1,5],12],[[6,6,1,11],4],
   [[9,9,1,18],4],[[18,18,1,37],12]]);
AssertEqual("D206/H301 complete rows",
  branch206H301.complete_collected_rows_n_e_f_d_with_multiplicity,
  [[[2,1,2,0],4],[[12,6,2,11],5],[[18,9,2,18],4],[[36,18,2,37],5]]);
AssertEqual("D206/H303 complete rows",
  branch206H303.complete_collected_rows_n_e_f_d_with_multiplicity,
  [[[4,2,2,1],2],[[6,3,2,5],6],[[12,6,2,11],2],
   [[18,9,2,18],2],[[36,18,2,37],6]]);
AssertEqual("D140/H301 prime count",branch140H301.double_coset_count,36);
AssertEqual("D140/H303 prime count",branch140H303.double_coset_count,36);
AssertEqual("D206/H301 prime count",branch206H301.double_coset_count,18);
AssertEqual("D206/H303 prime count",branch206H303.double_coset_count,18);

branch140 := rec(
  fields := [
    rec(field := "H301", table := branch140H301),
    rec(field := "H303", table := branch140H303)
  ],
  label := "D140",
  structure := branch140Structure
);;
branch206 := rec(
  fields := [
    rec(field := "H301", table := branch206H301),
    rec(field := "H303", table := branch206H303)
  ],
  label := "D206",
  structure := branch206Structure
);;

projection := rec(
  G2_gassmann_minimality := rec(
    all_350_subgroup_classes := inventory,
    collision_bucket_indices := duplicateDegrees,
    durable_field_subgroup_invariants := [field301,field303],
    exact_11_collision_buckets := duplicateBuckets,
    full_permutation_character_equality := true,
    minimum_collision_index := Minimum(duplicateDegrees),
    table_of_marks_name := "U4(2).2",
    tom_subgroup_class_count := Length(tomOrders),
    unique_minimum_index320_bucket := [301,303]
  ),
  G4_global_arithmetic := rec(
    common_conductor_exponents_p3_p5_A_B := conductors,
    common_field_discriminant_decimal_no_newline_digits := 11658,
    common_field_discriminant_decimal_no_newline_sha256 :=
      "7f3ed0f731e5905f9af8254df2114ad15c2bb7d96cfa9a8b464a58ae8ea3ae70",
    common_field_discriminant_factorization := [
      [3,624],[5,496],[181,192],[283,160],[997,192],[1801,160],
      [2346241,192],
      [14932047182473291995860108491583652133938007263719,160]
    ],
    common_field_discriminant_positive := true,
    exact_eight_prime_support := [
      3,5,181,283,997,1801,2346241,
      14932047182473291995860108491583652133938007263719
    ],
    local_orbit_counts_I3_P3_Q3_I5_P5_C3_reflection_Cinf := rec(
      H301 := counts301,
      H303 := counts303,
      local_tom_indices := localTomIndices
    ),
    signature_r1_r2 := signature
  ),
  G5_tom140_local_algebra := rec(
    complete_H301_table := branch140H301,
    complete_H303_table := branch140H303,
    degree_one_factor_counts_H301_H303 := [8,0],
    finite_etale_Q3_algebras_nonisomorphic := true,
    structure := branch140Structure
  ),
  G6_tom206_local_algebra := rec(
    complete_H301_table := branch206H301,
    complete_H303_table := branch206H303,
    d3_branch_selected := false,
    finite_etale_Q3_algebras_nonisomorphic := true,
    structure := branch206Structure,
    unramified_quadratic_factor_counts_H301_H303 := [4,0]
  ),
  action := rec(carrier_degree := 27,generator_count := 6,
    weyl_order := Size(W27)),
  contract_alignment := rec(
    certificate_payload_top_level_keys := [
      "artifact_contract","G0_released_authority_rebind",
      "G1_primitive_orbit_resolvents","G2_gassmann_minimality",
      "G3_fixed_fields_and_zeta","G4_global_arithmetic",
      "G5_tom140_local_algebra","G6_tom206_local_algebra",
      "G7_independence_scope_release","written_bridges",
      "backend_contract","source_contract","scope_nonclaims",
      "nonresults","status"
    ],
    planned_code_inventory := [
      "README.md","c59_atomic_promote.py","c59_checker.py",
      "c59_checker_group.g","c59_checker_resolvent.py","c59_exact.py",
      "c59_group.py","c59_hash_manifest.py","c59_pipeline.py",
      "c59_producer.py","c59_resolvent.py","run_all.sh","test_c59.py"
    ],
    planned_result_inventory := [
      "RESULTS.md","TEST_REPORT.md","c59_certificate.json",
      "c59_check_report.json","c59_group_evidence.json",
      "c59_resolvent_evidence.json","c59_schema.json",
      "scoped_hash_manifest.json"
    ],
    scaled_integral_invariant_notation := "eta_i",
    scaled_line_coordinate_notation := "alpha_i=L*d_i",
    scaled_relation := "eta_i=L^2*tilde_eta_i",
    unscaled_invariant_notation := "tilde_eta_i"
  ),
  schema_id := "hcs-c59-checker-group-projection-v1",
  software := rec(
    ctbllib := PackageInfo("CTblLib")[1].Version,
    gap := GAPInfo.Version,
    smallgrp := PackageInfo("SmallGrp")[1].Version,
    tomlib := PackageInfo("TomLib")[1].Version
  ),
  status := "PASS"
);;

# All emitted strings are controlled ASCII identifiers/version strings.  This
# minimal canonical serializer sorts record keys and emits no whitespace.
JsonString := function(value)
  return Concatenation("\"",value,"\"");
end;;
Json := function(value)
  local names,name,parts;
  if IsBool(value) then
    if value then return "true"; else return "false"; fi;
  elif IsInt(value) then
    return String(value);
  elif IsString(value) then
    return JsonString(value);
  elif IsRecord(value) then
    names := SortedList(RecNames(value));
    parts := [];
    for name in names do
      Add(parts,Concatenation(JsonString(name),":",Json(value.(name))));
    od;
    return Concatenation("{",JoinStringsWithSeparator(parts,","),"}");
  elif IsList(value) then
    return Concatenation("[",JoinStringsWithSeparator(List(value,Json),","),"]");
  fi;
  Error("unsupported JSON leaf in checker projection");
end;;

# C60 successor: compare and transport the two order-324 normalizers.
N301 := Normalizer(W27,H301);;
N303 := Normalizer(W27,H303);;
nConjugate := IsConjugate(W27,N301,N303);;
nRepresentative := PermList(NormalizerConjugatorArray);;
if not nConjugate or N303^nRepresentative <> N301 then
  Error("frozen normalizer transport changed");
fi;
H303c := H303^nRepresentative;;
FrozenN301 := Group(List(N301Arrays,PermList));;
FrozenH302 := Group(List(H302Arrays,PermList));;
FrozenJ := Group(List(JArrays,PermList));;
AssertEqual("frozen N301",FrozenN301,N301);

IndexTwoRows := function(N)
  local rows,C,R;
  rows := [];;
  C := ConjugacyClassesSubgroups(N);;
  for R in List(C,Representative) do
    if Size(R)=Size(N)/2 then
      Add(rows,rec(
        abelian_invariants := AbelianInvariants(R),
        derived_order := Size(DerivedSubgroup(R)),
        id_group := IdGroup(R),
        is_normal := IsNormal(N,R),
        tom_locator_in_W := TomIndexOfFrozen(R)
      ));
    fi;
  od;
  SortBy(rows,row -> [row.tom_locator_in_W,row.id_group]);
  return rows;
end;;

CollisionNormalizerScan := function(buckets)
  local rows,bucket,left,right,Nleft,Nright,conjugate,x,rightc,J;
  rows := [];
  for bucket in buckets do
    left := TomImage(bucket[1]);
    right := TomImage(bucket[2]);
    Nleft := Normalizer(W27,left);
    Nright := Normalizer(W27,right);
    conjugate := IsConjugate(W27,Nleft,Nright);
    J := fail;
    if conjugate then
      x := RepresentativeAction(W27,Nright,Nleft,OnPoints);
      rightc := right^x;
      J := Intersection(left,rightc);
    fi;
    Add(rows,rec(
      bucket := bucket,
      field_degree := Index(W27,left),
      subgroup_order := Size(left),
      normalizer_orders := [Size(Nleft),Size(Nright)],
      normalizer_indices_over_subgroups :=
        [Index(Nleft,left),Index(Nright,right)],
      normalizer_tom_locators :=
        [TomIndexOfFrozen(Nleft),TomIndexOfFrozen(Nright)],
      normalizers_conjugate_in_W := conjugate,
      normalizers_conjugate_and_index_two_over_both :=
        conjugate and
        [Index(Nleft,left),Index(Nright,right)]=[2,2]
    ));
    if conjugate then
      rows[Length(rows)].transported_intersection_order := Size(J);
      rows[Length(rows)].transported_generated_order := Size(Group(
        Concatenation(GeneratorsOfGroup(left),GeneratorsOfGroup(rightc))));
      rows[Length(rows)].transported_intersection_tom_locator :=
        TomIndexOfFrozen(J);
    fi;
  od;
  return rows;
end;;

PermArray := p -> List([1..27],i -> i^p);;
GroupGeneratorArrays := H -> List(GeneratorsOfGroup(H),PermArray);;

VariableOrbitCounts := function(field)
  local action;
  action := ActionHomomorphism(W27,RightCosets(W27,field),OnRight);
  return List(localSubgroups,subgroup ->
    Length(Orbits(Image(action,subgroup),[1..Index(W27,field)])));
end;;

ArithmeticReport := function(field)
  local degree,counts,conductors,signature;
  degree := Index(W27,field);
  counts := VariableOrbitCounts(field);
  conductors := [
    degree-counts[1]+(degree-counts[2])/2+(degree-counts[3]),
    degree-counts[4]+3*(degree-counts[5])/4,
    degree-counts[6],
    degree-counts[7]
  ];
  signature := [2*counts[8]-degree,degree-counts[8]];
  return rec(
    conductor_exponents_p3_p5_A_B := conductors,
    degree := degree,
    orbit_counts_I3_P3_Q3_I5_P5_C3_C2_Cinf := counts,
    signature_r1_r2 := signature
  );
end;;

VariableLocalRows := function(field,D,I,P,Q)
  local action,Dimage,Iimage,Pimage,Qimage,Dorbits,rawRows,orbit,n,f,
        pOrbits,qOrbits,e,conductor,different,collected;
  action := ActionHomomorphism(W27,RightCosets(W27,field),OnRight);
  Dimage := Image(action,D);
  Iimage := Image(action,I);
  Pimage := Image(action,P);
  Qimage := Image(action,Q);
  Dorbits := Orbits(Dimage,[1..Index(W27,field)]);
  rawRows := [];
  for orbit in Dorbits do
    n := Length(orbit);
    f := Length(Orbits(Iimage,orbit));
    pOrbits := Length(Orbits(Pimage,orbit));
    qOrbits := Length(Orbits(Qimage,orbit));
    e := n/f;
    conductor := n-f+(n-pOrbits)/2+(n-qOrbits);
    different := conductor/f;
    Add(rawRows,[n,e,f,different]);
  od;
  Sort(rawRows);
  collected := Collected(rawRows);
  return rec(
    rows_n_e_f_d_with_multiplicity := collected,
    degree_total := Sum(collected,row -> row[2]*row[1][1]),
    different_total := Sum(collected,row -> row[2]*row[1][3]*row[1][4]),
    factor_count := Length(Dorbits)
  );
end;;

RelativeImageSizes := function(S,T,H,quotientOrder)
  local decompImage,inertiaImage,e,f,g;
  decompImage := Size(Group(Concatenation(GeneratorsOfGroup(S),
    GeneratorsOfGroup(H))))/Size(H);
  inertiaImage := Size(Group(Concatenation(GeneratorsOfGroup(T),
    GeneratorsOfGroup(H))))/Size(H);
  e := inertiaImage;
  f := decompImage/inertiaImage;
  g := quotientOrder/decompImage;
  if not IsInt(e) or not IsInt(f) or not IsInt(g) or g*e*f<>quotientOrder then
    Error("relative tower row failed");
  fi;
  return [g,e,f];
end;;

AbsoluteLocalAtCoset := function(D,I,P,Q,H,g)
  local S,T,U,V,n,e,f,pCount,qCount,conductor,different;
  S := Intersection(H,D^(g^-1));
  T := Intersection(H,I^(g^-1));
  U := Intersection(H,P^(g^-1));
  V := Intersection(H,Q^(g^-1));
  n := Size(D)/Size(S);
  e := Size(I)/Size(T);
  f := n/e;
  pCount := Size(D)*Size(U)/(Size(P)*Size(S));
  qCount := Size(D)*Size(V)/(Size(Q)*Size(S));
  conductor := n-f+(n-pCount)/2+(n-qCount);
  different := conductor/f;
  if not IsInt(n) or not IsInt(e) or not IsInt(f) or not IsInt(different)
      or n<>e*f then
    Error("absolute tower local row failed");
  fi;
  return [n,e,f,different];
end;;

RelativeTowerRows := function(D,I,P,Q,N,Hs,J)
  local cosets,orbits,raw,orbit,coset,g,S,T,base,relative,absolute,
        quotientOrders,position,row;
  cosets := RightCosets(W27,N);
  orbits := OrbitsDomain(D,cosets,OnRight);
  raw := [];
  for orbit in orbits do
    coset := orbit[1];
    g := Representative(coset);
    S := Intersection(N,D^(g^-1));
    T := Intersection(N,I^(g^-1));
    base := AbsoluteLocalAtCoset(D,I,P,Q,N,g);
    relative := List(Hs,H -> RelativeImageSizes(S,T,H,2));
    Add(relative,RelativeImageSizes(S,T,J,4));
    absolute := List(Hs,H -> AbsoluteLocalAtCoset(D,I,P,Q,H,g));
    Add(absolute,AbsoluteLocalAtCoset(D,I,P,Q,J,g));
    quotientOrders := [2,2,2,4];
    for position in [1..4] do
      row := relative[position];
      Add(row,absolute[position][4]-row[2]*base[4]);
      if row[4] < 0 or row[1]*row[2]*row[3]<>quotientOrders[position]
          or absolute[position][2]<>row[2]*base[2] then
        Error("relative different/tower identity failed");
      fi;
    od;
    Add(raw,[base,relative]);
  od;
  Sort(raw);
  return rec(
    base_prime_count := Length(orbits),
    collected_base_n_e_f_d_and_relative_g_e_f_d_H301_H302_H303_J := Collected(raw),
    relative_factor_counts_H301_H302_H303_J := List([1..4],position ->
      Sum(raw,row -> row[2][position][1])),
    rows_base_n_e_f_d_then_relative_g_e_f_d_H301_H302_H303_J := raw
  );
end;;

pilot := rec(
  H301_normal_in_N301 := IsNormal(N301,H301),
  H303_normal_in_N303 := IsNormal(N303,H303),
  N301_abelian_invariants := AbelianInvariants(N301),
  N301_derived_order := Size(DerivedSubgroup(N301)),
  N301_id_group := IdGroup(N301),
  N301_index := Index(W27,N301),
  N301_order := Size(N301),
  N301_tom_locator := TomIndexOfFrozen(N301),
  N303_abelian_invariants := AbelianInvariants(N303),
  N303_derived_order := Size(DerivedSubgroup(N303)),
  N303_id_group := IdGroup(N303),
  N303_index := Index(W27,N303),
  N303_order := Size(N303),
  N303_tom_locator := TomIndexOfFrozen(N303),
  normalizers_conjugate_in_W := nConjugate,
  normalizers_equal_as_embedded_groups := N301=N303,
  tom_permutation_characters_equal :=
    permutationCharacters[TomIndexOfFrozen(N301)] =
    permutationCharacters[TomIndexOfFrozen(N303)],
  N301_index_two_subgroup_classes := IndexTwoRows(N301),
  N303_index_two_subgroup_classes := IndexTwoRows(N303)
);;
pilot.all_11_collision_normalizer_scan :=
  CollisionNormalizerScan(expectedDuplicateBuckets);;
if nConjugate then
  pilot.H303_conjugate_contained_in_N301 := IsSubgroup(N301,H303c);;
  pilot.H301_H303c_intersection_order := Size(Intersection(H301,H303c));;
  pilot.H301_H303c_generated_order := Size(Group(Concatenation(
    GeneratorsOfGroup(H301),GeneratorsOfGroup(H303c))));;
  pilot.H301_equals_H303c := H301=H303c;;
  pilot.H301_H303c_tom_locators :=
    [TomIndexOfFrozen(H301),TomIndexOfFrozen(H303c)];;
  indexTwo := Filtered(List(ConjugacyClassesSubgroups(N301),Representative),
    R -> Size(R)=162);;
  SortBy(indexTwo,TomIndexOfFrozen);;
  H302 := indexTwo[2];;
  J := Intersection(H301,H303c);;
  AssertEqual("frozen H302",FrozenH302,H302);
  AssertEqual("frozen J",FrozenJ,J);
  pilot.normalizer_conjugating_permutation_one_based := PermArray(nRepresentative);;
  pilot.N301_generators_one_based := GroupGeneratorArrays(N301);;
  pilot.H302_generators_one_based := GroupGeneratorArrays(H302);;
  pilot.J_generators_one_based := GroupGeneratorArrays(J);;
  pilot.J_equals_N301_derived_subgroup := J=DerivedSubgroup(N301);;
  pilot.J_normal_in_N301 := IsNormal(N301,J);;
  pilot.N301_over_J_id_group := IdGroup(FactorGroup(N301,J));;
  pilot.J_equals_all_pairwise_index_two_intersections :=
    ForAll(Combinations(indexTwo,2),pair -> Intersection(pair[1],pair[2])=J);;
  pilot.J_core_order_in_W := Size(Core(W27,J));;
  pilot.J_index_in_W := Index(W27,J);;
  pilot.J_normalizer_order_in_W := Size(Normalizer(W27,J));;
  pilot.J_tom_locator := TomIndexOfFrozen(J);;
  pilot.N301_core_order_in_W := Size(Core(W27,N301));;
  pilot.N301_normalizer_order_in_W := Size(Normalizer(W27,N301));;
  pilot.index_two_locators_in_common_N := List(indexTwo,TomIndexOfFrozen);;
  pilot.index_two_core_orders_in_W := List(indexTwo,H -> Size(Core(W27,H)));;
  pilot.index_two_global_normalizer_orders :=
    List(indexTwo,H -> Size(Normalizer(W27,H)));;
  pilot.index_two_global_normalizers_equal_common_N :=
    List(indexTwo,H -> Normalizer(W27,H)=N301);;
  pilot.index_two_pairwise_intersection_orders :=
    List(Combinations(indexTwo,2),pair -> Size(Intersection(pair[1],pair[2])));;
  pilot.index_two_pairwise_generated_orders :=
    List(Combinations(indexTwo,2),pair -> Size(Group(Concatenation(
      GeneratorsOfGroup(pair[1]),GeneratorsOfGroup(pair[2])))));;
  pilot.arithmetic_N_degree160 := ArithmeticReport(N301);;
  pilot.arithmetic_H301_degree320 := ArithmeticReport(H301);;
  pilot.arithmetic_H302_degree320 := ArithmeticReport(H302);;
  pilot.arithmetic_H303c_degree320 := ArithmeticReport(H303c);;
  pilot.arithmetic_J_degree640 := ArithmeticReport(J);;
  pilot.local_D140_N := VariableLocalRows(N301,D140,I140,P140,Q140);;
  pilot.local_D140_H302 := VariableLocalRows(H302,D140,I140,P140,Q140);;
  pilot.local_D140_J := VariableLocalRows(J,D140,I140,P140,Q140);;
  pilot.local_D206_N := VariableLocalRows(N301,D206,I206,P206,Q206);;
  pilot.local_D206_H302 := VariableLocalRows(H302,D206,I206,P206,Q206);;
  pilot.local_D206_J := VariableLocalRows(J,D206,I206,P206,Q206);;
  pilot.relative_tower_D140 := RelativeTowerRows(D140,I140,P140,Q140,
    N301,[H301,H302,H303c],J);;
  pilot.relative_tower_D206 := RelativeTowerRows(D206,I206,P206,Q206,
    N301,[H301,H302,H303c],J);;
  pilot.H301_H302_character_equal :=
    permutationCharacters[301]=permutationCharacters[302];;
  pilot.H301_H303_character_equal :=
    permutationCharacters[301]=permutationCharacters[303];;
  pilot.V4_Brauer_character_relation :=
    permutationCharacters[266]+2*permutationCharacters[327] =
    permutationCharacters[301]+permutationCharacters[302]+
    permutationCharacters[303];;
fi;
DiscriminantReport := function(label,field)
  local report,exponents,support,factorization,position,exponent;
  report := ArithmeticReport(field);
  exponents := report.conductor_exponents_p3_p5_A_B;
  support := [
    [3,1],[5,2],[181,3],[283,4],[997,3],[1801,4],
    [2346241,3],
    [14932047182473291995860108491583652133938007263719,4]
  ];
  factorization := [];
  for position in support do
    exponent := exponents[position[2]];
    Add(factorization,[position[1],exponent]);
  od;
  report.field := label;
  report.discriminant_factorization := factorization;
  report.discriminant_positive := true;
  return report;
end;;

TowerFieldRow := function(label,H,tomIndex)
  return rec(
    abelian_invariants := AbelianInvariants(H),
    core_order_in_W := Size(Core(W27,H)),
    derived_order := Size(DerivedSubgroup(H)),
    field_degree := Index(W27,H),
    generators_one_based := GroupGeneratorArrays(H),
    id_group := IdGroup(H),
    label := label,
    normal_in_N := IsNormal(N301,H),
    normalizer_equals_N := Normalizer(W27,H)=N301,
    order := Size(H),
    tom_locator := tomIndex
  );
end;;

CanonicalPointPartition := function(H)
  local blocks;
  blocks := List(OrbitsDomain(H,[1..27],OnPoints),Set);
  Sort(blocks);
  return blocks;
end;;

CanonicalPairPartition := function(H)
  local blocks;
  blocks := List(OrbitsDomain(H,Combinations([1..27],2),OnSets),Set);
  Sort(blocks);
  return blocks;
end;;

TransportPointPartition := function(partition,x)
  local blocks;
  blocks := List(partition,block -> Set(List(block,i -> i^x)));
  Sort(blocks);
  return blocks;
end;;

TransportPairPartition := function(partition,x)
  local blocks;
  blocks := List(partition,block -> Set(List(block,pair -> OnSets(pair,x))));
  Sort(blocks);
  return blocks;
end;;

NPointPartition := CanonicalPointPartition(N301);;
NPairPartition := CanonicalPairPartition(N301);;
H302PointPartition := CanonicalPointPartition(FrozenH302);;
H302PairPartition := CanonicalPairPartition(FrozenH302);;
N303PointPartition := CanonicalPointPartition(N303);;
N303PairPartition := CanonicalPairPartition(N303);;
transportedN303PointPartition :=
  TransportPointPartition(N303PointPartition,nRepresentative);;
transportedN303PairPartition :=
  TransportPairPartition(N303PairPartition,nRepresentative);;
AssertEqual("transported N303 point partition",transportedN303PointPartition,
  NPointPartition);
AssertEqual("transported N303 pair partition",transportedN303PairPartition,
  NPairPartition);
AssertEqual("H302 point partition equals N",H302PointPartition,NPointPartition);
AssertEqual("H302 pair partition equals N",H302PairPartition,NPairPartition);
transportEquationAll := ForAll(Elements(N303),h -> ForAll([1..27],i ->
  (i^h)^nRepresentative = (i^nRepresentative)^(h^nRepresentative)));;
AssertEqual("right-action label transport equation",transportEquationAll,true);

characterVectors := rec(
  H301 := List(ValuesOfClassFunction(permutationCharacters[301]),Int),
  H302 := List(ValuesOfClassFunction(permutationCharacters[302]),Int),
  H303 := List(ValuesOfClassFunction(permutationCharacters[303]),Int),
  J := List(ValuesOfClassFunction(permutationCharacters[266]),Int),
  N := List(ValuesOfClassFunction(permutationCharacters[327]),Int)
);;
AssertEqual("V4 Brauer vector identity",
  List([1..Length(characterVectors.N)],i ->
    characterVectors.J[i]+2*characterVectors.N[i]-
    characterVectors.H301[i]-characterVectors.H302[i]-
    characterVectors.H303[i]),
  List([1..Length(characterVectors.N)],i -> 0));

local140H301 := VariableLocalRows(H301,D140,I140,P140,Q140);;
local140H303 := VariableLocalRows(H303c,D140,I140,P140,Q140);;
local206H301 := VariableLocalRows(H301,D206,I206,P206,Q206);;
local206H303 := VariableLocalRows(H303c,D206,I206,P206,Q206);;

collisionRows := pilot.all_11_collision_normalizer_scan;;
qualifyingCollisionBuckets := List(Filtered(collisionRows,row ->
  row.normalizers_conjugate_and_index_two_over_both),row -> row.bucket);;
AssertEqual("unique collision with conjugate index-two normalizers",
  qualifyingCollisionBuckets, [[301,303]]);

projection60 := rec(
  action := rec(carrier_degree := 27,generator_count := 6,
    weyl_order := Size(W27)),
  coefficient_orbit_partitions := rec(
    field_order := ["N","H301","H302","H303","J"],
    H302_pair_partition_equals_N := H302PairPartition=NPairPartition,
    H302_point_partition_equals_N := H302PointPartition=NPointPartition,
    pair_partitions := [
      NPairPartition,CanonicalPairPartition(H301),
      H302PairPartition,CanonicalPairPartition(H303c),
      CanonicalPairPartition(J)
    ],
    point_partitions := [
      NPointPartition,CanonicalPointPartition(H301),
      H302PointPartition,CanonicalPointPartition(H303c),
      CanonicalPointPartition(J)
    ],
    transported_N303_pair_partition := transportedN303PairPartition,
    transported_N303_pair_partition_equals_N :=
      transportedN303PairPartition=NPairPartition,
    transported_N303_point_partition := transportedN303PointPartition,
    transported_N303_point_partition_equals_N :=
      transportedN303PointPartition=NPointPartition
  ),
  character_relation := rec(
    class_count := Length(characterVectors.N),
    class_sizes := SizesConjugacyClasses(ct),
    coefficient_order_H301_H302_H303_J_N := [-1,-1,-1,1,2],
    H301_equals_H303 := characterVectors.H301=characterVectors.H303,
    H301_equals_H302 := characterVectors.H301=characterVectors.H302,
    relation_zero_on_every_class := true,
    vectors := characterVectors
  ),
  collision_normalizer_scan := rec(
    exact_11_collision_buckets := expectedDuplicateBuckets,
    qualifying_buckets_normalizers_conjugate_and_index_two_over_both :=
      qualifyingCollisionBuckets,
    rows := collisionRows
  ),
  frozen_permutation_arrays := rec(
    branch140_D_generators := Branch140DArrays,
    branch140_P_generators := Branch140PArrays,
    branch140_Q_generators := Branch140QArrays,
    branch206_D_generators := Branch206DArrays,
    branch206_I_generators := Branch206IArrays,
    branch206_P_generators := Branch206PArrays,
    branch206_Q_generators := Branch206QArrays,
    H301_generators := H301Arrays,
    H302_generators := H302Arrays,
    H303_generators := H303Arrays,
    J_generators := JArrays,
    N_generators := N301Arrays,
    normalizer_conjugator := NormalizerConjugatorArray,
    W27_generators := W27Arrays
  ),
  global_arithmetic := rec(
    exact_prime_support := [
      3,5,181,283,997,1801,2346241,
      14932047182473291995860108491583652133938007263719
    ],
    fields := [
      DiscriminantReport("N",N301),
      DiscriminantReport("H301",H301),
      DiscriminantReport("H302",H302),
      DiscriminantReport("H303",H303c),
      DiscriminantReport("J",J)
    ],
    local_subgroup_tom_order_I3_P3_Q3_I5_P5_C3_C2_Cinf :=
      localTomIndices
  ),
  local_arithmetic := rec(
    relative_field_order := ["H301","H302","H303","J"],
    tom140 := rec(
      absolute_tables := [
        rec(field := "N",table := pilot.local_D140_N),
        rec(field := "H301",table := local140H301),
        rec(field := "H302",table := pilot.local_D140_H302),
        rec(field := "H303",table := local140H303),
        rec(field := "J",table := pilot.local_D140_J)
      ],
      decomposition_tom_locator := 140,
      relative_tower_over_N := pilot.relative_tower_D140
    ),
    tom206 := rec(
      absolute_tables := [
        rec(field := "N",table := pilot.local_D206_N),
        rec(field := "H301",table := local206H301),
        rec(field := "H302",table := pilot.local_D206_H302),
        rec(field := "H303",table := local206H303),
        rec(field := "J",table := pilot.local_D206_J)
      ],
      decomposition_tom_locator := 206,
      relative_tower_over_N := pilot.relative_tower_D206
    )
  ),
  normalizer_tower := rec(
    common_normalizer := rec(
      abelian_invariants := AbelianInvariants(N301),
      core_order_in_W := Size(Core(W27,N301)),
      derived_order := Size(DerivedSubgroup(N301)),
      id_group := IdGroup(N301),
      index_in_W := Index(W27,N301),
      normalizer_order_in_W := Size(Normalizer(W27,N301)),
      order := Size(N301),
      quotient_by_J_id_group := IdGroup(FactorGroup(N301,J)),
      tom_locator := TomIndexOfFrozen(N301)
    ),
    fields := [
      TowerFieldRow("H301",H301,301),
      TowerFieldRow("H302",H302,302),
      TowerFieldRow("H303",H303c,303)
    ],
    intersection := rec(
      core_order_in_W := Size(Core(W27,J)),
      equals_derived_subgroup_of_N := J=DerivedSubgroup(N301),
      generators_one_based := GroupGeneratorArrays(J),
      index_in_W := Index(W27,J),
      normal_in_N := IsNormal(N301,J),
      normalizer_order_in_W := Size(Normalizer(W27,J)),
      order := Size(J),
      tom_locator := TomIndexOfFrozen(J)
    ),
    normalizer_transport := rec(
      conjugating_permutation_one_based := NormalizerConjugatorArray,
      conjugating_permutation_inverse_one_based :=
        PermArray(nRepresentative^-1),
      H303_transport_contained_in_N := IsSubgroup(N301,H303c),
      right_action_equation := "(i^h)^x=(i^x)^(h^x)",
      right_action_equation_checked_pairs := Size(N303)*27,
      right_action_equation_holds := transportEquationAll,
      source_N303_generators_one_based := GroupGeneratorArrays(N303),
      transported_N303_generators_one_based :=
        GroupGeneratorArrays(N303^nRepresentative),
      transported_normalizer_equals_N := N303^nRepresentative=N301
    ),
    pairwise_generated_orders := pilot.index_two_pairwise_generated_orders,
    pairwise_intersection_orders := pilot.index_two_pairwise_intersection_orders,
    pairwise_intersections_equal_J :=
      pilot.J_equals_all_pairwise_index_two_intersections
  ),
  schema_id := "hcs-c60-gap-normalizer-projection-v1",
  software := rec(
    ctbllib := PackageInfo("CTblLib")[1].Version,
    gap := GAPInfo.Version,
    smallgrp := PackageInfo("SmallGrp")[1].Version,
    tomlib := PackageInfo("TomLib")[1].Version
  ),
  status := "PASS"
);;

jsonOutput := OutputTextUser();;
SetPrintFormattingStatus(jsonOutput,false);;
PrintTo(jsonOutput,Json(projection60),"\n");
CloseStream(jsonOutput);;
QUIT_GAP(0);
