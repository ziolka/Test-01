from setuptools import setup


def do_setup(args_dict):
    setup(name= args_dict.get("name"),
      version= args_dict.get("version"),
      description= args_dict.get("description"),
      url= args_dict.get("url"),
      author= args_dict.get("author"),
      author_email= args_dict.get("author_email"),
      license= args_dict.get("license"),
      packages= args_dict.get("packages"),
         )
