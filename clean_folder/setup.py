from setuptools import setup

setup(name='clean-folder',
      version='0.0.1',
      description='Sort fieles in folders',
      author='Olexandr Chepkanych',
      author_email='a.chepkanich@gmail.com',
      license='MIT',
      entry_points= {'console_scripts': ['clean-folder = clean_folder.clean:normalize']}
      )