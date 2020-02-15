Release instructions
====================

These are just notes for releasing the software.

1. Bump version numbers in ``setup.py`` and ``docs/conf.py``.
2. Remove past build artifacts::

     rm -r build dist

3. Build the packages::

     python3 setup.py sdist bdist_wheel

4. Upload the packages to PyPI::

     python3 -m twine upload dist/*

5. Build the docs::

     cd docs
     make html latexpdf
     tar cvf struct-parse-<VERSION>-html.tar.gz _build/html

6. Create a new Github release.

   - Create a tag with the new version number.
   - Describe the changes in the release notes.
   - Attach the build artifacts.
   - Attach the docs (HTML zip and PDF).
