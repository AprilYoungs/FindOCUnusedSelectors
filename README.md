# FindOCUnusedSelectors
Scan and list Objective-C unused selectors

### How it work
**Get all methods**:We can find all the Objective-C methods from **linkMap**<br>
**Get all used selector**: Export used selector from MachO file with this command<br>
`otool -v -s __DATA __objc_selrefs machOFile`<br>
**Unused methods**: unused methods = All methods - used methods

### How to use it
Open ununsedSel.py and change the setting
``` python
outPath = "./TestData/export" #result export directory
machOFilePath = "./TestData/TestDemo" #executable-file
linkmapPath = "./TestData/TestDemo-linkMap.txt" #linkMap.txt

# selectors to ignore from scan
ignoreMeths = [".cxx_destruct", ".cxx_construct"]
# prefix of your module, if you want to scan all module, set this to ""
prefix = "AY"
```

run the python script with 
```
python3 ununsedSel.py
```

For more detail [How to find all the unused Objective-C selector](https://aprilyoungs.github.io/blog/2020/03/31/ios_UnusedMethods)
