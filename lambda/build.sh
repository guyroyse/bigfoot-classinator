rm classinator.zip
zip -r classinator.zip *.py
cd lib/python3.6/site-packages
for f in [a-z]*
do
    zip -r ../../../classinator.zip $f
done
cd ../../..