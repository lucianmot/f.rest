# Forest - key words & syntax propositions

This file contains the propositions for the FOREST's syntax.

#### Assignment to variables, integers, floats, arrays and hashes

```
a = 1
return a

BACKPACK a PACKED WITH 1 OAK_SEEDLING(S)
EXPLORE BACKPACK a

Forest >>> 1 OAK SEEDLING(S)
```

```{PACKED WITH : = } ``` assignment operator =
```{BACKPACK a : a}``` variables considered as backpacks; we can have multiple variables / backpacks hence, the name a
```{1 SEEDLING : 1}``` numbers considered OAK_SEEDLING(S)
```{EXPLORE : explicit return}```

```
a = 1.5
return a

BACKPACK a PACKED WITH 1.5 PINE_SEEDLING(S)
EXPLORE BACKPACK a

Forest >>> 1.5 PINE_SEEDLING(S)

```
```{ 1.5 PINE_SEEDLING(S) : 1.5 }``` floats considered as PINE_SEEDLING(S)

```{RANGER'S_JEEP : ARRAY}```


#### IF statements & booleans

```
IF a = 3
return True

WALK_THIS_FOREST_PATH_IF_SEE BACKPACK a PACEKD WITH 3 OAK_SEEDLING(S)
EXPLORE TREES
```

```
IF [3, 1.2]
return False

WALK_THIS_FOREST_PATH_IF_SEE RANGER'S JEEP PACKED WITH 3 OAK_SEEDLING(S) and 1.2 PINE_SEEDLING(S)
EXPLORE FOREST_FLOWERS
```


```{WALK_THIS_FOREST_PATH_IF_SEE : IF}```
```{WALK_THIS_FOREST_PATH_IF_SEE : ELSIF}``` the same as IF
```{WALK_THIS_FOREST_PATH_IF_DID_NOT_SEE : ELSE}```

#### LOOPS

```{WALK_IN_THE_CIRCLE_THROUGH_THE_FOREST : FOR }```
```{RUN_IN_THE_CIRCLE_THROUGH_THE_FOREST : WHILE }```

---

 

### Usage

**Variable assignment**  

```
BACKPACK:myvar^PACK_WITH^<<poop>> 

// echo^myvar should print poop
```

---

### Error message ideas


