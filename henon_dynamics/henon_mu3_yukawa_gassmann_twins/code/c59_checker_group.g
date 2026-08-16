# Independent GAP reconstruction for the staged C59 GROUP lane.
#
# The field subgroups and both p=3 branches below are defined only by frozen
# one-based permutations on the released 27-line carrier.  TomLib is used as
# a verified conjugacy-class locator and as the exhaustive source of the 350
# transitive permutation characters; no IsomorphismGroups image defines a
# field in this checker.

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

jsonOutput := OutputTextUser();;
SetPrintFormattingStatus(jsonOutput,false);;
PrintTo(jsonOutput,Json(projection),"\n");
CloseStream(jsonOutput);;
QUIT_GAP(0);
