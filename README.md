# Learning-Notes
```
cd book
rm -r _build
jupyter-book build --all ./
ghp-import -n -p -f _build/html
rm -r _build

cd ..
git add .
git commit -m "test1"
git push origin main
open -a "Google Chrome" https://github.com/Jinzhao-Yu/Learning-Notes/deployments/
```
