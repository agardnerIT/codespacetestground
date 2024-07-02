# codespacetestground

## Documentation Website

### Installation
```
pip install mkdocs
mkdocs serve -a localhost:9000
# Site available on 
```

### Serving Locally / Development
```
mkdocs serve -a localhost:9000
# Site available at: http://localhost:9000
```

### Building and Uploading

```
mkdocs build --site-dir=site
git add site/*
git commit -m "update docs"
git push
```

A GitHub action (`github/.workflows/static.yml`) will then pick up those files and deploy to GitHub Pages.