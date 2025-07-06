import segno

link = input('Enter the Text or Url: ')
fileName = input('Enter the filename: ')

qr = segno.make(link)
qr.save(fileName +'.png', scale=100)

print(f'qr code saved as {fileName}.png')