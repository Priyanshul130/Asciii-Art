
from PIL import Image,ImageDraw
#open and  show the image
img=Image.open("photo.jpeg")
img.show()

#resize the image
width,height=img.size
aspect_ratio= height/width
new_width=80

#height is calculated as per aspect ratio
#/2 to reduce the numbar of pixels for the picture we are using
new_height=aspect_ratio*new_width*0.50

img=img.resize((new_width,int(new_height)))

#convert image to grey scale
img=img.convert("L")


#get pixels details
pixels=img.getdata()

#replace each pixels with a charactor
char=["#","&","@","%","?","!",":",";",",","."," "]
new_pixels=""

for pixel in pixels:
    pixel=char[pixel//25]#index is calculated in buckets of 25
    new_pixels+=pixel

#split tring of char into multiple strings of len
#=to new width  and height
new_pixel_count=len(new_pixels)
final_image=""
for index in range(0,new_pixel_count,new_width):
    row=new_pixels[index:(index+new_width)]

    final_image+="\n"+row

#printimg image on screen
print(final_image)


#create a jpg image file
img=Image.new("RGB",(1000,1000),(255,255,255))#image of size 100*100 and white background
draw=ImageDraw.Draw(img)

#convert to text
draw.text((250,150),final_image,(0,0,0))
#black charactor
img.show()
img.save("image.jpg")

#write to text file
with open ("ascaii.text","w")as f:
    f.write(final_image)






    
    
    


    
    















          
