import os
for dirpath, dnames, fnames in os.walk("/fs/class-projects/spring2024/gems497/ge497g00/lidc-cancerous"):
    for f in fnames:
        if f.endswith(".npy"):
            os.rename(os.path.join(dirpath, f), "/fs/class-projects/spring2024/gems497/ge497g00/cancerous/" + f)
