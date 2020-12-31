# Instructions

1. Create a local python environment and activate it
```shell
python3 -m venv myenv
source myenv/bin/activate
```

2. Install packages
```shell
pip3 install -r requirements.txt
```
If you are having issues with the firebase package, then do:
```shell
pip3 uninstall python-firebase
pip3 install git+https://github.com/ozgur/python-firebase
```

3. Update config file to include Firebase Realtime Database URL
```yaml
data_source_url: https://restcountries.eu/rest/v2/all
firebase_db_url: https://#YOUR_FIREBASE_PROJECT_NAME#.firebaseio.com/
```

4. Run program -- the python-firebase package may have some memory leaking issues.
Disable all warnings while running.
```shell
python3 -W ignore main.py
```

5. Check your firebase realtime database in your firebase project.