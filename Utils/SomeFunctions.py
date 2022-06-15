def get_list_from(location):
    """Can be used to get data from txt files stored in Assets"""
    with open(f"Assets/{location}.txt") as file:
        listt = file.readlines()
    return listt
    
def get_list(filename):
  """Can be used to get data from txt files stored in Assets/Gracie"""
  with open(f"Assets/Gracie/{filename}.txt") as file:
    listt = file.readlines()
  return listt