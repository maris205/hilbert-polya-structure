# Independent GAP/TomLib reconstruction for the staged C61 group component.
#
# This call graph does not read the Python evidence or any selection-pilot data.
# It enumerates all double cosets before checking counts; no degree/order target
# filter is used to discover rows.  Its only output is canonical compact JSON.

if GAPInfo.Version <> "4.11.1" then Error("frozen GAP version changed"); fi;
if LoadPackage("tomlib") <> true then Error("TomLib is required"); fi;
if LoadPackage("ctbllib") <> true then Error("CTblLib is required"); fi;
if PackageInfo("TomLib")[1].Version <> "1.2.9" then Error("TomLib version changed"); fi;
if PackageInfo("CTblLib")[1].Version <> "1.3.1" then Error("CTblLib version changed"); fi;
SizeScreen([1000000,1000000]);;

AssertEqual := function(label,got,expected)
  if got <> expected then
    Error(Concatenation(label," changed: got ",String(got),", expected ",String(expected)));
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
HplusArrays := [
  [1,2,19,21,20,3,24,11,9,10,23,15,13,14,22,5,4,18,6,16,17,12,8,27,25,26,7],
  [16,27,13,12,22,26,15,25,24,7,14,18,20,5,1,23,8,17,9,19,6,2,10,3,4,21,11],
  [26,13,22,20,24,15,21,3,14,1,19,11,25,18,23,7,5,9,12,27,16,8,6,17,2,10,4]
];;
HminusArrays := [
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
I5Arrays := [
  [16,23,27,8,26,9,7,11,24,10,25,5,13,6,12,20,2,18,19,22,17,1,21,14,4,15,3],
  [16,2,23,8,18,17,25,4,21,10,11,12,22,27,26,1,6,5,19,20,9,13,3,24,7,15,14]
];;
P5Arrays := [[10,7,3,14,4,6,1,12,5,13,15,17,2,19,21,8,27,25,9,11,24,23,26,20,22,18,16]];;
C3Arrays := [[23,25,18,22,17,21,1,14,4,15,12,19,2,20,16,10,24,27,11,8,26,9,7,5,13,6,3]];;
C2Arrays := [[1,2,3,6,5,4,7,8,11,10,9,12,15,14,13,18,17,16,21,20,19,22,23,24,27,26,25]];;
CinfArrays := [[6,13,16,12,5,1,18,15,20,22,26,4,2,17,8,3,14,7,19,9,27,10,24,23,25,11,21]];;
P3WitnessArray := [25,22,23,27,24,26,9,13,20,16,19,7,11,8,10,15,12,14,18,21,17,4,1,2,6,3,5];;

W := Group(List(W27Arrays,PermList));;
Hplus := Group(List(HplusArrays,PermList));;
Hminus := Group(List(HminusArrays,PermList));;
AssertEqual("W/H orders",[Size(W),Size(Hplus),Size(Hminus)],[51840,162,162]);
WElements := Elements(W);;
naturalAction := ActionHomomorphism(W,[1..27],OnPoints);;
AssertEqual("distinct labelled W permutations",Length(Set(WElements)),51840);
AssertEqual("faithful labelled W action",Size(Kernel(naturalAction)),1);

PermArray27 := p -> List([1..27],i -> i^p);;

CanonicalRightCosetArrays := function(G,H)
  local rows,C;
  rows := [];
  for C in RightCosets(G,H) do
    Add(rows,Minimum(List(Elements(C),PermArray27)));
  od;
  Sort(rows);
  return rows;
end;;

TensorRows := function(G,L,R,lane)
  local rightCosets,rows,D,array,g,Q,I,J,seed,row;
  rightCosets := CanonicalRightCosetArrays(G,R);
  rows := [];
  # Python's functional left action h o g is GAP right multiplication g*h;
  # hence its L-orbits on canonical R-right-cosets are GAP R\G/L.
  for D in DoubleCosets(G,R,L) do
    array := Minimum(List(Elements(D),PermArray27));
    g := PermList(array);
    seed := Position(rightCosets,array)-1;
    # GAP multiplies right actions oppositely to the Python functional arrays:
    # R^g has functional arrays g o R o g^-1, exactly the source convention.
    Q := R^g;
    I := Intersection(L,Q);
    J := Group(Concatenation(GeneratorsOfGroup(L),GeneratorsOfGroup(Q)));
    row := rec(
      base_degree := Index(G,J),
      intersection := I,
      intersection_order := Size(I),
      join := J,
      join_order := Size(J),
      lane := lane,
      orbit_size := Size(L)/Size(I),
      representative_one_based := array,
      seed := seed,
      simple_degree := Index(G,I)
    );
    Add(rows,row);
  od;
  SortBy(rows,row -> [row.simple_degree,row.seed]);
  AssertEqual(Concatenation(lane," all double cosets retained"),Length(rows),12);
  AssertEqual(Concatenation(lane," dimension"),Sum(rows,row -> row.simple_degree),102400);
  return rows;
end;;

rowsPP := TensorRows(W,Hplus,Hplus,"Tpp");;
rowsPM := TensorRows(W,Hplus,Hminus,"Tpm");;
rowsMM := TensorRows(W,Hminus,Hminus,"Tmm");;
allRows := Concatenation(rowsPP,rowsPM,rowsMM);;

qClasses := [];; pClasses := [];;
for row in allRows do
  position := PositionProperty(qClasses,R -> IsConjugate(W,row.intersection,R));
  if position=fail then Add(qClasses,row.intersection); position:=Length(qClasses); fi;
  row.q_type := position;
  position := PositionProperty(pClasses,R -> IsConjugate(W,row.join,R));
  if position=fail then Add(pClasses,row.join); position:=Length(pClasses); fi;
  row.p_type := position;
od;
AssertEqual("unified Q/P counts",[Length(qClasses),Length(pClasses)],[18,8]);

CompactRow := function(row)
  return rec(
    base_degree := row.base_degree,
    core_intersection_order := Size(Core(W,row.intersection)),
    core_join_order := Size(Core(W,row.join)),
    intersection_automorphism_order := Size(Normalizer(W,row.intersection))/Size(row.intersection),
    intersection_normalizer_order := Size(Normalizer(W,row.intersection)),
    intersection_order := row.intersection_order,
    join_automorphism_order := Size(Normalizer(W,row.join))/Size(row.join),
    join_normalizer_order := Size(Normalizer(W,row.join)),
    join_order := row.join_order,
    lane := row.lane,
    orbit_size := row.orbit_size,
    p_type := row.p_type,
    q_type := row.q_type,
    representative_one_based := row.representative_one_based,
    seed := row.seed,
    simple_degree := row.simple_degree
  );
end;;

# Independent TomLib character and local-locator projection.
tom := TableOfMarks("U4(2).2");;
tomGroup := UnderlyingGroup(tom);;
toW := IsomorphismGroups(tomGroup,W);;
if toW=fail or not IsBijective(toW) then Error("TomLib carrier location failed"); fi;
tomOrders := OrdersTom(tom);;
ct := CharacterTable("U4(2).2");;
permchars := PermCharsTom(ct,tom);;
TomImage := index -> Image(toW,RepresentativeTom(tom,index));;
TomIndex := function(H)
  local index;
  for index in [1..Length(tomOrders)] do
    if tomOrders[index]=Size(H) and IsConjugate(W,H,TomImage(index)) then return index; fi;
  od;
  Error("subgroup absent from TableOfMarks");
end;;
hpTom := TomIndex(Hplus);; hmTom := TomIndex(Hminus);;
AssertEqual("H+/H- ToM",[hpTom,hmTom],[301,303]);
charPlus := List(ValuesOfClassFunction(permchars[hpTom]),Int);;
charMinus := List(ValuesOfClassFunction(permchars[hmTom]),Int);;
AssertEqual("Gassmann character",charPlus,charMinus);
tensorCharacter := List(charPlus,x -> x*x);;

localGroups := [
  Group(List(Branch140DArrays,PermList)),
  Group(List(Branch140PArrays,PermList)),
  Group(List(Branch140QArrays,PermList)),
  Group(List(Branch206DArrays,PermList)),
  Group(List(Branch206IArrays,PermList)),
  Group(List(Branch206PArrays,PermList)),
  Group(List(Branch206QArrays,PermList)),
  Group(List(I5Arrays,PermList)),Group(List(P5Arrays,PermList)),
  Group(List(C3Arrays,PermList)),Group(List(C2Arrays,PermList)),
  Group(List(CinfArrays,PermList))
];;
localLabels := ["D140","P140","Q140","D206","I206","P206","Q206","I5","P5","C3","C2","Cinf"];;
localExpectedTom := [140,72,7,206,140,72,7,147,23,6,2,5];;
AssertEqual("local ToM locators",List(localGroups,TomIndex),localExpectedTom);
localRows := List([1..Length(localGroups)],i -> rec(
  generators_one_based := List(GeneratorsOfGroup(localGroups[i]),PermArray27),
  label := localLabels[i],order := Size(localGroups[i]),tom_locator := localExpectedTom[i]
));;

ClassPosition := function(classes,H)
  local position;
  position := PositionProperty(classes,R -> IsConjugate(W,H,R));
  if position=fail then Error("relative subgroup absent from unified classes"); fi;
  return position;
end;;

# Full 160-position mixed orbit census, independently from the 12 factor rows.
Nminus := Normalizer(W,Hminus);;
conjugatorArrays := CanonicalRightCosetArrays(W,Nminus);;
conjugates := List(conjugatorArrays,array -> Hminus^PermList(array));;
AssertEqual("160 distinct H- conjugates",Length(Set(conjugates)),160);
unseen := [1..160];; relativeRows := [];;
while Length(unseen)>0 do
  seed := Minimum(unseen);
  Q := conjugates[seed];
  orbit := [];
  for h in Elements(Hplus) do AddSet(orbit,Position(conjugates,Q^h)); od;
  if fail in orbit or not IsSubset(unseen,orbit) then Error("relative orbit partition failed"); fi;
  SubtractSet(unseen,orbit);
  I := Intersection(Hplus,Q);
  J := Group(Concatenation(GeneratorsOfGroup(Hplus),GeneratorsOfGroup(Q)));
  Add(relativeRows,rec(
    base_degree := Index(W,J),intersection_order := Size(I),join_order := Size(J),
    p_type := ClassPosition(pClasses,J),
    q_type := ClassPosition(qClasses,I),
    raw_count := Length(orbit),representative_conjugate_index := seed-1,
    simple_degree := Index(W,I)
  ));
od;
SortBy(relativeRows,row -> [row.simple_degree,row.base_degree,row.raw_count,row.representative_conjugate_index]);
AssertEqual("relative-position type count",Length(relativeRows),8);
AssertEqual("relative-position population",Sum(relativeRows,row -> row.raw_count),160);

plusP3 := First(rowsPP,row -> row.seed=69).join;;
minusP3 := First(rowsMM,row -> row.seed=86).join;;
mixedP6 := First(rowsPM,row -> row.seed=149).join;;
witness := PermList(P3WitnessArray);;
AssertEqual("exact P3 complete-set witness",minusP3^witness,plusP3);
if IsConjugate(W,plusP3,mixedP6) then Error("P3 unexpectedly conjugate to P6"); fi;

JsonString := function(value) return Concatenation("\"",value,"\""); end;;
Json := function(value)
  local names,name,parts;
  if IsBool(value) then if value then return "true"; else return "false"; fi;
  elif IsInt(value) then return String(value);
  elif IsString(value) then return JsonString(value);
  elif IsRecord(value) then
    names:=SortedList(RecNames(value)); parts:=[];
    for name in names do Add(parts,Concatenation(JsonString(name),":",Json(value.(name)))); od;
    return Concatenation("{",JoinStringsWithSeparator(parts,","),"}");
  elif IsList(value) then return Concatenation("[",JoinStringsWithSeparator(List(value,Json),","),"]");
  fi;
  Error("unsupported JSON leaf");
end;;

projection := rec(
  ambient := rec(
    W_permutation_count := Size(W),
    W_distinct_labelled_permutation_count := Length(Set(WElements)),
    labelled_W_action_faithful := Size(Kernel(naturalAction)) = 1
  ),
  burnside := rec(
    common_character_values_on_25_classes := charPlus,
    common_tensor_character_values_on_25_classes := tensorCharacter,
    all_three_linearizations_equal := true,
    Hplus_Hminus_nonconjugate := not IsConjugate(W,Hplus,Hminus)
  ),
  local_subgroups := localRows,
  mixed := rec(
    conjugate_count := Length(conjugates),
    conjugator_arrays_one_based := conjugatorArrays,
    relative_position_rows := relativeRows,
    relative_type_count := Length(relativeRows)
  ),
  p3_p6 := rec(
    exact_witness_one_based := P3WitnessArray,
    witness_complete_set_equality := true,
    P3_nonconjugate_to_P6 := true
  ),
  rows := rec(
    Tpp := List(rowsPP,CompactRow),Tpm := List(rowsPM,CompactRow),Tmm := List(rowsMM,CompactRow)
  ),
  schema_id := "hcs-c61-gap-group-projection-v1",
  software := rec(ctbllib:=PackageInfo("CTblLib")[1].Version,gap:=GAPInfo.Version,tomlib:=PackageInfo("TomLib")[1].Version),
  status := "PASS",
  target_degree_or_order_filters_used := false,
  type_counts := rec(P:=Length(pClasses),Q:=Length(qClasses))
);;
jsonOutput := OutputTextUser();;
SetPrintFormattingStatus(jsonOutput,false);;
PrintTo(jsonOutput,Json(projection),"\n");
CloseStream(jsonOutput);;
QUIT_GAP(0);
