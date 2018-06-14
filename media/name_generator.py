import uuid
def generate_name(filename):
  return "{}/{}/{}".format(
    "uploads",
    uuid.uuid4(),
    filename
  )