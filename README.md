# getMetaData
Get meta data from any file : 
get more information on how to use this. Please refer below thread.

https://stackoverflow.com/questions/21697645/how-to-extract-metadata-from-a-image-using-python/57621166#57621166

for Windows and mac: it is availble at https://www.sno.phy.queensu.ca/~phil/exiftool/

mac user :

install the Exiftool.dmg file into mac,
use it directly in terminal using the command "exiftool" "filePath"


for linux :
1. You can install ExifTool on Ubuntu using the apt utility
sudo apt install libimage-exiftool-perl

2. From Source
You can compile and install ExifTool from the source on any Linux distro (including CentOS)
$ wget https://netix.dl.sourceforge.net/project/exiftool/Image-ExifTool-10.61.tar.gz
$ tar xvf Image-ExifTool-10.61.tar.gz
$ cd Image-ExifTool-10.61/ 

You can run ExifTool by running ./exiftool in the ExifTool directory or proceed to the next step if you want to install it system-wide. You must have Perl installed on your Linux box before compiling.

```perl Makefile.PL
make
make test
make install
```
You can now run ExifTool anywhere in your terminal by typing exiftool.

Using ExifTool with Metadata
Here are the most common commands you can use with ExifTool:

Showing all the metadata associated with an image

```$ exiftool IMG.CR2
ExifTool Version Number : 10.61
 File Name : IMG.CR2
 Directory : .
 File Size : 16 MB
 File Modification Date/Time : 2017:09:24 12:15:41+00:00
 File Access Date/Time : 2017:09:24 12:16:16+00:00
 File Inode Change Date/Time : 2017:09:24 12:16:10+00:00
 File Permissions : rw-rw-r--
 File Type : CR2
 File Type Extension : cr2
 MIME Type : image/x-canon-cr2
```
source : https://linoxide.com/linux-how-to/install-use-exiftool-linux-ubuntu-centos/






