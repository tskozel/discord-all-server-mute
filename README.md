# Python script to mute all servers on Discord
Warning: this will not work with two-factor auth.

### Dependencies
discord.py v.1.0.1
json (built-in)
### Installation
```bash
python3 -m pip install -U -r requirements.txt
chmod +x ./main.py 
./main.py
```
The Windows folks need to do this:
```cmd
py -3 -m pip install -U -r requirements.txt
py -3 main.py
``` 
### Usage
```
./main.py -l "test@example.com" -p "example_password1234"
```
On Windows, just replace the slash with backslash \\