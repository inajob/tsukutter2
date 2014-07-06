cd bat
python update.py
python publish.py
cd ..

git add raw_data/*.txt
git add data/*.txt
git add index.html
git add current.json
git commit -m 're.sh'
git push origin gh-pages
