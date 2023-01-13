# unused-css

Find unused CSS and Sass classes in a React or Angular project.

UnusedCSS for Angular finds unused CSS classes in your components.
It also checks if there are unused classes in Sass partials and global stylesheets ("\_foo.scss", "index.css" etc.)

The CLI outputs a list of the unused CSS classes and it **DOES NOT** modify anyfile.

To run navigate to a React/Angular src folder and run:

```
python3 unused.py
```

Or pass the project src folder absolute path as an argument:

```
python3 unused.py /Users/me/project/src
```
