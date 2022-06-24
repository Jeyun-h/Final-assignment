from textwrap import fill
from turtle import color, pencolor
import PySimpleGUI as sg
import io
from PIL import Image, ImageDraw

file_type = [
    ("JPEG (*.jpg)", "*.jpg")
]

pen_colors = {
    "Black" : "black",
    "White" : "white",
    "Blue" : "blue",
    "Red" : "red",
    "Green" : "green",
    "Yellow" : "yellow"
}
bg_colors = {
    "Black" : "black",
    "White" : "white",
    "Blue" : "blue",
    "Red" : "red",
    "Green" : "green",
    "Yellow" : "yellow"
}

def main():
    pen_colors_names = list(pen_colors.keys())
    bg_colors_names = list(bg_colors.keys())
    layout = [
        [sg.Image(key="-IMAGE-", size = (400,400), background_color="white")],
        [sg.Text("         "),sg.Button("up",size=(4,2))],
        [sg.Button("<",size=(4,2)),sg.Button("ON",size=(4,2)),sg.Button(">",size=(4,2))],
        [sg.Text("         "),sg.Button("down",size=(4,2))],
        [sg.Text("펜 색상 :"), sg.Combo(pen_colors_names, default_value="Black", key = "-PEN-",enable_events=True,readonly=True),
        sg.Text("배경 색상 :"), sg.Combo(bg_colors_names, default_value="White", key = "-BG-",enable_events=True,readonly=True)],
        [sg.Text("이미지 파일 : "), sg.Input(size=(25,1), key = "-FILENAME_ONE-"), sg.FileBrowse(file_types = file_type)],
        [sg.Button("이미지를 불러온다")],
        [sg.Button("이미지 저장")]
    ]
    
    window = sg.Window("그림을 그리는 프로그램", layout, size = (450,700))
    
    image_target = window["-IMAGE-"]
    
    points=[(0,0)]
    point_num=0
    pencol="black"
    bgcol="white"
    
    # image = Image.new("RGB",(400,400), "yellow")
    # bio = io.BytesIO()
    # image.save(bio, format="PNG")
            # image_target.update(data = bio.getvalue(), size=(400, 400)) 
    
    
    while True:
        event, values = window.read()
        
        print(event,values)
                
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        
        filename_one = values ["-FILENAME_ONE-"]
        pen =  values ["-PEN-"]
        bg =  values ["-BG-"]
        
        if event == "up" :
            points+=[(points[point_num][0],points[point_num][1]-20)]
            point_num+=1
            image = Image.new("RGB",(400,400), bgcol)
            bio = io.BytesIO()
            image.save(bio, format="PNG")
            image_target.update(data = bio.getvalue(), size=(400, 400))
            draw = ImageDraw.Draw(image)
            draw.line( points, width = 10, fill = pencol, joint="curve")
            bio = io.BytesIO()
            image.save(bio, format="PNG")
            image_target.update(data = bio.getvalue(), size=(400, 400))
            
        if event == "down" :
            points+=[(points[point_num][0],points[point_num][1]+20)]
            point_num+=1
            image = Image.new("RGB",(400,400), bgcol)
            bio = io.BytesIO()
            image.save(bio, format="PNG")
            image_target.update(data = bio.getvalue(), size=(400, 400))
            draw = ImageDraw.Draw(image)
            draw.line( points, width = 10, fill = pencol, joint="curve")
            bio = io.BytesIO()
            image.save(bio, format="PNG")
            image_target.update(data = bio.getvalue(), size=(400, 400))
            
        if event == ">" :
            points+=[(points[point_num][0]+20,points[point_num][1])]
            point_num+=1
            image = Image.new("RGB",(400,400), bgcol)
            bio = io.BytesIO()
            image.save(bio, format="PNG")
            image_target.update(data = bio.getvalue(), size=(400, 400))
            draw = ImageDraw.Draw(image)
            draw.line( points, width = 10, fill = pencol, joint="curve")
            bio = io.BytesIO()
            image.save(bio, format="PNG")
            image_target.update(data = bio.getvalue(), size=(400, 400))
            
        if event == "<" :
            points+=[(points[point_num][0]-20,points[point_num][1])]
            point_num+=1
            image = Image.new("RGB",(400,400), bgcol)
            bio = io.BytesIO()
            image.save(bio, format="PNG")
            image_target.update(data = bio.getvalue(), size=(400, 400))
            draw = ImageDraw.Draw(image)
            draw.line( points, width = 10, fill = pencol, joint="curve")
            bio = io.BytesIO()
            image.save(bio, format="PNG")
            image_target.update(data = bio.getvalue(), size=(400, 400))
            
        if pen == "White":
            pencol= "white"
            image = Image.new("RGB",(400,400), bgcol)
            bio = io.BytesIO()
            image.save(bio, format="PNG")
            image_target.update(data = bio.getvalue(), size=(400, 400))
            draw = ImageDraw.Draw(image)
            draw.line( points, width = 10, fill = pencol, joint="curve")
            bio = io.BytesIO()
            image.save(bio, format="PNG")
            image_target.update(data = bio.getvalue(), size=(400, 400))
            
        if pen == "Black":
            pencol= "black"
            image = Image.new("RGB",(400,400), bgcol)
            bio = io.BytesIO()
            image.save(bio, format="PNG")
            image_target.update(data = bio.getvalue(), size=(400, 400))
            draw = ImageDraw.Draw(image)
            draw.line( points, width = 10, fill = pencol, joint="curve")
            bio = io.BytesIO()
            image.save(bio, format="PNG")
            image_target.update(data = bio.getvalue(), size=(400, 400))
            
        if pen == "Blue":
            pencol= "blue"
            image = Image.new("RGB",(400,400), bgcol)
            bio = io.BytesIO()
            image.save(bio, format="PNG")
            image_target.update(data = bio.getvalue(), size=(400, 400))
            draw = ImageDraw.Draw(image)
            draw.line( points, width = 10, fill = pencol, joint="curve")
            bio = io.BytesIO()
            image.save(bio, format="PNG")
            image_target.update(data = bio.getvalue(), size=(400, 400))
            
        if pen == "Red":
            pencol= "red"
            image = Image.new("RGB",(400,400), bgcol)
            bio = io.BytesIO()
            image.save(bio, format="PNG")
            image_target.update(data = bio.getvalue(), size=(400, 400))
            draw = ImageDraw.Draw(image)
            draw.line( points, width = 10, fill = pencol, joint="curve")
            bio = io.BytesIO()
            image.save(bio, format="PNG")
            image_target.update(data = bio.getvalue(), size=(400, 400))
            
        if pen == "Green":
            pencol= "green"
            image = Image.new("RGB",(400,400), bgcol)
            bio = io.BytesIO()
            image.save(bio, format="PNG")
            image_target.update(data = bio.getvalue(), size=(400, 400))
            draw = ImageDraw.Draw(image)
            draw.line( points, width = 10, fill = pencol, joint="curve")
            bio = io.BytesIO()
            image.save(bio, format="PNG")
            image_target.update(data = bio.getvalue(), size=(400, 400))
            
        if pen == "Yellow":
            pencol= "yellow"
            image = Image.new("RGB",(400,400), bgcol)
            bio = io.BytesIO()
            image.save(bio, format="PNG")
            image_target.update(data = bio.getvalue(), size=(400, 400))
            draw = ImageDraw.Draw(image)
            draw.line( points, width = 10, fill = pencol, joint="curve")
            bio = io.BytesIO()
            image.save(bio, format="PNG")
            image_target.update(data = bio.getvalue(), size=(400, 400))
            
        if bg == "White":
            bgcol= "white"
            image = Image.new("RGB",(400,400), bgcol)
            bio = io.BytesIO()
            image.save(bio, format="PNG")
            image_target.update(data = bio.getvalue(), size=(400, 400))
            draw = ImageDraw.Draw(image)
            draw.line( points, width = 10, fill = pencol, joint="curve")
            bio = io.BytesIO()
            image.save(bio, format="PNG")
            image_target.update(data = bio.getvalue(), size=(400, 400))
            
        if bg == "Black":
            bgcol= "black"
            image = Image.new("RGB",(400,400), bgcol)
            bio = io.BytesIO()
            image.save(bio, format="PNG")
            image_target.update(data = bio.getvalue(), size=(400, 400))
            draw = ImageDraw.Draw(image)
            draw.line( points, width = 10, fill = pencol, joint="curve")
            bio = io.BytesIO()
            image.save(bio, format="PNG")
            image_target.update(data = bio.getvalue(), size=(400, 400))
            
        if bg == "Yellow":
            bgcol= "yellow"
            image = Image.new("RGB",(400,400), bgcol)
            bio = io.BytesIO()
            image.save(bio, format="PNG")
            image_target.update(data = bio.getvalue(), size=(400, 400))
            draw = ImageDraw.Draw(image)
            draw.line( points, width = 10, fill = pencol, joint="curve")
            bio = io.BytesIO()
            image.save(bio, format="PNG")
            image_target.update(data = bio.getvalue(), size=(400, 400))
            
        if bg == "Green":
            bgcol= "green"
            image = Image.new("RGB",(400,400), bgcol)
            bio = io.BytesIO()
            image.save(bio, format="PNG")
            image_target.update(data = bio.getvalue(), size=(400, 400))
            draw = ImageDraw.Draw(image)
            draw.line( points, width = 10, fill = pencol, joint="curve")
            bio = io.BytesIO()
            image.save(bio, format="PNG")
            image_target.update(data = bio.getvalue(), size=(400, 400))
            
        if bg == "Blue":
            bgcol= "blue"
            image = Image.new("RGB",(400,400), bgcol)
            bio = io.BytesIO()
            image.save(bio, format="PNG")
            image_target.update(data = bio.getvalue(), size=(400, 400))
            draw = ImageDraw.Draw(image)
            draw.line( points, width = 10, fill = pencol, joint="curve")
            bio = io.BytesIO()
            image.save(bio, format="PNG")
            image_target.update(data = bio.getvalue(), size=(400, 400))
            
        if bg == "Red":
            bgcol= "red"
            image = Image.new("RGB",(400,400), bgcol)
            bio = io.BytesIO()
            image.save(bio, format="PNG")
            image_target.update(data = bio.getvalue(), size=(400, 400))
            draw = ImageDraw.Draw(image)
            draw.line( points, width = 10, fill = pencol, joint="curve")
            bio = io.BytesIO()
            image.save(bio, format="PNG")
            image_target.update(data = bio.getvalue(), size=(400, 400))
        
        print(points,point_num)
        
        if event == "이미지를 불러온다" :
            image = Image.open(filename_one)
            image.thumbnail( (400, 400) )
            bio = io.BytesIO()
            image.save(bio, format="PNG")
            image_target.update(data = bio.getvalue(), size=(400, 400))
        


if __name__ == "__main__":
    main()