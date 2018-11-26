
def make_migrate():
    print("MIGRATION")
    from Common.models import migrator

    from playhouse.migrate import migrate, CharField, FloatField, IntegerField

    migrations = []
    for elt in migrations:
        try:
            migrate(elt)
        except Exception as e:
            print(e)
