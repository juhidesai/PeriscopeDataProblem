import os
def read_file():
    f = open(os.path.join(os.getcwd(),"input.txt"))
    dirt_patches = {}
    instructions = ""
    line = f.readline().strip()
    roomx = int(line.split(" ")[0])
    roomy = int(line.split(" ")[1])
    line = f.readline().strip()
    hooverx = int(line.split(" ")[0])
    hoovery = int(line.split(" ")[1])
    line = f.readline().strip()
    while(line):
        l = len(line.split(" "))
        if l > 1:
##            it is a dirt patch entry
            patchx = int(line.split(" ")[0])
            patchy = int(line.split(" ")[1])
            if patchx in dirt_patches:
                dirt_patches[patchx].append(patchy)
            else:
                dirt_patches[patchx] = [patchy]
        else:
            instructions = line
            break
        line = f.readline().strip()
    f.close()
    return dirt_patches, instructions, roomx, roomy, hooverx, hoovery
        
def traverse(dirt_patches, i, roomx, roomy, hooverx, hoovery, dirt_count):    
    if i == 'N':
        if hoovery == roomy-1:
            return hooverx, hoovery, dirt_count
        hoovery += 1
    elif i == 'S':
        if hoovery == 0:
            return hooverx, hoovery, dirt_count
        hoovery -= 1 
    elif i == 'E':
        if hooverx == roomx-1:
            return hooverx, hoovery, dirt_count
        hooverx += 1
    elif i == 'W':
        if hooverx == 0:
            return hooverx, hoovery, dirt_count
        hooverx -= 1            
    dirt_count = clean_dirt(hooverx, hoovery, dirt_count, dirt_patches)
    return hooverx, hoovery, dirt_count

def clean_dirt(hooverx, hoovery, dirt_count, dirt_patches):
    if hooverx in dirt_patches and hoovery in dirt_patches[hooverx]:
        dirt_count += 1
        dirt_patches[hooverx].remove(hoovery)
    return dirt_count
    
def roomba():
    dirt_patches, instructions, roomx, roomy, hooverx, hoovery = read_file()
    dirt_count = 0
    for instruction in instructions:        
        hooverx, hoovery, dirt_count = traverse(dirt_patches, instruction, roomx, roomy, hooverx, hoovery, dirt_count)
##        print instruction, hooverx, hoovery
##    print "The number of dirt patches cleaned are: ",dirt_count
##    print "The hoover is at position: (",hooverx,", ",hoovery,")"
    print hooverx,hoovery
    print dirt_count
if __name__ == "__main__":
    roomba()
