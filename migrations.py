
def make_migrate():
    from Common.models import migrator

    from playhouse.migrate import migrate, CharField, FloatField, IntegerField

    migrations = []
    for elt in migrations:
        print("MIGRATION : ", elt)
        try:
            migrate(elt)
        except Exception as e:
            print(e)
