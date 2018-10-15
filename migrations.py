
def make_migrate():
    print("MIGRATION")
    from Common.models import migrator

    from playhouse.migrate import migrate, CharField, FloatField, IntegerField

    migrations = []

    for x, y, z in migrations:
        try:
            migrate(migrator.add_column(x, y, z))
            print(x, " : ", y)
        except Exception as e:
            print(e)
