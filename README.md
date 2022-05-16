# Learning-Notes
This is the learning notes of Jinzhao, containing all things that I'm trying to handle.\

- Everytime change the contents, run the code below in the terminal
- preview the result
```
cd book
rm -r _build
jupyter-book build --all ./
cp -R images _build/html/images
open -a "Google Chrome" _build/html/index.html
```
- Push the final book on the GitHub
```
ghp-import -n -p -f _build/html
rm -r _build

cd ..
git add .
git commit -m "update log"
git push origin main
open -a "Google Chrome" https://github.com/Jinzhao-Yu/Learning-Notes/deployments/
```
