import re


pattern = re.compile(r'([0-9]+\.*[0-9]*)rpx')

with open("public.css","w+")as o:
    with open('public.css', 'r') as f:
        line = f.readline()
        while line:
            a=pattern.findall(line)
            if(len(a)>=1):
                num=float(a[0])
                num=num/2



                c=pattern.sub(str(num)+"px",line)
                o.writelines(c)


            #print line
            else:
                o.writelines(line)

            line = f.readline()