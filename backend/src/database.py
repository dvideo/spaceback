class Database:
  next_id = 1

  def __init__(self):
    self.records = {}

  def list(self):
    return list(self.records.values())

  def find(self, id):
    return self.records[id]

  def create(self, record):
    record['id'] = Database.next_id
    Database.next_id += 1

    self.records[record['id']] = record
    return record

  def update(self, id, attrs):
    self.records[id].update(attrs)
    return self.records[id]

  def destroy(self, id):
    if self.records[id] is not None:
      del self.records[id]