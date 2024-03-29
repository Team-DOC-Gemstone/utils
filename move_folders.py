import os
folders = [os.path.join(os.getcwd(), "", x)
           for x in os.listdir(".")
]
for item in folders:
    if not "py" in item and not "folders" in item:
        arr = item.split('/')
        os.rename(item, item.split(arr[-1])[0] + "folders/" + arr[-1])
