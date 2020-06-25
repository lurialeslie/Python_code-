score = input("Enter Score:")
mark = float (score)
if 0 <= mark <= 1.0 :
  if mark >= 0.9 :
    print("A")
  elif mark >= 0.8 :
    print("B")
  elif mark >= 0.7 :
    print("C")
  elif mark >= 0.6 :
    print("D")
  elif mark <= 0.6 :
    print("F")
else :
    print("error")
    quit()
