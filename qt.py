import bg
import qt_er

bg.getimports()

gt = 'Closed with Quick Term'

print("Quick Terminal")
print("Cmds: ov, ex")
inp = input(">>")
if inp == 'ex':
    bg.getimports()
    quit(gt)
if inp == 'ov':
    qt_er.error1()