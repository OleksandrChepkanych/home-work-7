from setuptools import setup, find_namespace_packages

setup(name='clean-folder',
      version='0.0.4',
      description='Sort fieles in folders',
      author='Olexandr Chepkanych',
      author_email='a.chepkanich@gmail.com',
      license='MIT',
      packages=find_namespace_packages(),
      entry_points= {'console_scripts': ['clean-folder = clean_folder.clean:not_nul']}
      )