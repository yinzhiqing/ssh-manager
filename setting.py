##bvexchange config
#
from tomlbase import tomlbase

class tomlopt(tomlbase):
    def __init__(self, tomlfile):
        super().__init__(tomlfile)

    def __getattr__(self, name):
        return None

setting = tomlopt("conf.toml")


def run():
    print(setting.toml_file)


if __name__ == "__main__":
    run()
