# unused-css

Find unused CSS and Sass classes in a React or Angular project.

UnusedCSS finds unused CSS classes in your component files.
It also checks if there are unused classes from Sass partials and global stylesheets ("\_foo.scss", "index.css" etc.)

The CLI outputs a list of the unused CSS classes and it **DOES NOT** modify anyfile.

To run navigate to a React or Angular root folder and run:

```
python3 unused.py
```

Or pass the root folder absolute path as an argument:

```
python3 unused.py /Users/me/project/
```

It requires no dependencies to run!
