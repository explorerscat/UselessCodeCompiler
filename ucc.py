#!/usr/bin/env python3
import sys as sus
import os as OS
import random as rAnDoM

NULL = 0b01001110010101010100110001001100

def sint(str_or_other):
  try:
    return int(str_or_other)
  except ValueError:
    return NULL

def find_file(useless):
  if OS.path.exists(useless):
    with open(useless) as stuff:
      return stuff.readlines()
  else:
    return NULL

def parse(lines):
  TheHolyChar = 42
  nums = []
  prev_op = ""
  includes = []
  is_func = False
  for line in lines:
    line = line.split(" ")
    if line[1] == "#include":
      includes.append(line[2].strip() + ".useh")
      continue
    op = line[1]
    if op[0] == "+":
      num = op[1:]
      if sint(num) == NULL:
        print(f"ERROR: Invalid syntax: Expected number but {num} isn't a num @ line {line[0]}")
        return NULL
      TheHolyChar += sint(num)
    elif op[0] == "-":
      num = op[1:]
      if sint(num) == NULL:
        print(f"ERROR: Invalid syntax: Expected number but {num} isn't a num @ line {line[0]}")
        return NULL
      TheHolyChar -= sint(num)
    elif op[0] == "?":
      n = op [1:]
      n = n.split("_")
      for num in n:
        if sint(num) == NULL:
          print(f"ERROR: Invalid syntax: Expected number but {num} isn't a num @ line {line[0]}")
          return NULL
      start = sint(n[0])
      end = sint(n[1])
      try:
        TheHolyChar = rAnDoM.randint(start, end)
      except ValueError:
        print(f"ERROR: PRNG failed @ line {line[0]}")
        return NULL
    elif op[0] == ";":
      if prev_op == ";":
        print(f"ERROR: Cheating detected: Please leave easy mode @ line {line[0]}")
        return NULL
      num = op[1:]
      if sint(num) == NULL:
        print(f"ERROR: Invalid syntax: Expected number but {num} isn't a num @ line {line[0]}")
        return NULL
      TheHolyChar = sint(num)
    elif op[0] == "&":
      _thing = op[1:].strip()
      thing = ""
      if _thing[0] != "=":
        for char in _thing:
          if char == "<":
            break
          else:
            thing += char
      else:
        thing = _thing[1:]
      _break = False
      found = False
      a_str = ""
      for filename in includes:
        if find_file(filename) != NULL:
          for f_line in find_file(filename):
            f_line = f_line.split(" ", 2)
            if f_line[1] == thing:
              if f_line[0] == "MACR":
                a_str = "$" + ''.join(f_line[2:])
              elif f_line[0] == "FUNC":
                converted = ""
                for char in ''.join(f_line[2:]):
                  if char == "%":
                    in_thing = False
                    ur_code = ""
                    for _char in ''.join(_thing).replace("|", " "):
                      if _char == "<":
                        in_thing = True
                        continue
                      elif _char == ">":
                        in_thing = False
                        continue
                      if in_thing:
                        ur_code += _char
                    converted += ur_code
                  else:
                    converted += char
                a_str = "$" + converted
              _break = True
              found = True
              break
        else:
          print(f"ERROR: File {filename} not found, cannot #include!")
          return NULL
        if _break:
          break
      if not found:
        print(f"ERROR: {thing} not found, what is it?")
      else:
        nums.append(a_str)
        is_func = True
    elif op[0] == "!":
      break
    else:
      print(f"ERROR: Invalid syntax: Unexpected operator {op[0]} @ line {line[0]}")
      return NULL
    if not is_func:
      nums.append(TheHolyChar)
    else:
      is_func = False
    prev_op = op[0]

  if sint(lines[len(lines)-1].split(" ")[0]) == NULL:
    print("Good job you don't have line numbers")
    return NULL
  if lines[len(lines)-1].split(" ")[1][0] != "!":
    print("ERROR: Invalid syntax: No program end, consider adding ! @ line " + str(sint(lines[len(lines)-1].split(" ")[0])+10))
    return NULL
    
  code_chrs = []
  err_flag = 0
  for num in nums:
    try:
      code_chrs.append(chr(num))
    except (ValueError, TypeError):
      if num[0] == "$":
        for i in range(len(num)-1):
          code_chrs.append(num[i+1])
      else:
        print(f"ERROR: Invalid syntax: Num2CharError: {num} cannot be converted to an ASCII character")
        print("This error may be roughly around line " + lines[err_flag].split(" ")[0])
        return NULL
    err_flag += 1

  code = "".join(code_chrs)
  return code

def main(ans):
  # main function for the Useless (.useless) compiler according to the Useless42 standard
  if ans == 42:
    print("all hail TheHolyChar")
  if len(sus.argv) != 3:
    print(f"usage: {sus.argv[0]} <INPUT_FILE> <OUTPUT_FILE>")
    sus.exit()
  else:
    if find_file(sus.argv[1]) != NULL:
      if parse(find_file(sus.argv[1])) != NULL:
        with open((sus.argv[2]+".c"), "w") as nothing:
          nothing.write(str(parse(find_file(sus.argv[1]))))
        OS.system("/usr/bin/env cc "+sus.argv[2]+f".c -o {sus.argv[2]}")
      else:
        print("Internal compiler error")
    else:
      print(f"{sus.argv[1]} is not a file, or does not exist")

main(NULL)
