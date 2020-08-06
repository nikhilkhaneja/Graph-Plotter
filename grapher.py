import pygame, math, sys
from pygame import *
from math import *

pygame.init()

class TextOnScreen:
    ### Define class properties
    # Fonts
    # Title font
    font1 = font.SysFont('Orbitron', 40)

    # Instructions font
    #font2 = font.SysFont('Ariel', 24)
    font2 = font.SysFont('Verdana', 16)

    # Shortcuts font
    #font3 = font.SysFont('Times New Roman', 16)
    font3 = font.SysFont('Verdana', 14)

    # Equation font
    #font4 = font.SysFont('Times New Roman', 20)
    font6 = font.SysFont('Orbitron', 20)

    # Font for invalid equation entries
    font5 = font.SysFont('Verdana', 12)
    font4 = font.SysFont('Verdana', 20)

    # Constants
    instructionsWidth = 20
    shortcutsHeight = 0

    def title(self, screen, text, width, height):
        title = self.font1.render(text, 1, GrapherMain.yellow)
        screen.blit(title, (width, height))

    def instructions(self, screen, text, height):
        instructions = self.font2.render(text, 1, GrapherMain.white)
        screen.blit(instructions, (self.instructionsWidth, height))

    def shortcuts(self, screen, text, width, wNum):
        if wNum == 1:
            self.shortcutsHeight = 50
        elif wNum == 2:
            self.shortcutsHeight = 80
        elif wNum == 3:
            self.shortcutsHeight = 110
        elif wNum == 4:
            self.shortcutsHeight = 140
        elif wNum == 5:
            self.shortcutsHeight = 170
        elif wNum == 6:
            self.shortcutsHeight = 200
        elif wNum == 7:
            self.shortcutsHeight = 230
        elif wNum == 8:
            self.shortcutsHeight = 260

        self.shortcutsHeight += 230

        shortcuts = self.font4.render(text, 1, GrapherMain.white)
        screen.blit(shortcuts, (width, self.shortcutsHeight))


class GrapherMain:

    ### Define class properties

    # Colours
    white = (255, 255, 255)
    black = (0, 0, 0)
    lightBlue = (100, 250, 240)
    darkBlue = (20, 100, 220)
    blue = (51, 153, 255)
    orange = (255, 153, 51)
    red = (255, 0, 0)
    gray = (127, 127, 127)
    lightGray = (245, 245, 245)
    linesGray = (200, 200, 200)
    yellow = (255, 255, 0)
    bizare = (59, 59, 59)
    # Window size
    width = 1300
    extraWidth = 450
    height = 1000

    # Possible k values for graph resizing
    kValues = [2,5,10,15,20, 25, 50, 100, 150,200,250,300]
    kIndex = 6

    # Property linked to graph number
    graph = 1

    # Init method will run automatically when class is instantiated
    def __init__(self, Graphs, eq):
        screen = display.set_mode((self.width + self.extraWidth, self.height))

        # Name of standard window
        display.set_caption("Graph Plotter")
        screen.fill(self.yellow)

        ### Create the graph paper
        # k is the number of pixels per unit on the grid
        # k must always be a factor of width and height
        k = self.kValues[self.kIndex]

        COLOUR = self.black
        if Graphs == 1:
            screen.fill(self.black)
            self.graphPaper(k, screen)
            equation = []
            eq2 = ' '
        elif Graphs == 2:
            screen.set_clip(0, 0, self.extraWidth + self.width, self.height)
            screen.fill(self.black)
            screen.set_clip(None)
            self.graphPaper(k, screen)
            eq2 = eq
            equation = []
            self.plotLine(screen, k, eq2, self.orange)
        elif Graphs == 3:
            screen.set_clip(0, 0, self.extraWidth + self.width, self.height)
            screen.fill(self.black)
            screen.set_clip(None)
            self.graphPaper(k, screen)
            eq2 = eq
            equation = []
            self.plotLine(screen, k, eq2, self.orange)

        ### Create all text and blit on screen
        # Create an instance of TextOnScreen class
        screenOneInfo = TextOnScreen()

        # Create title
        screenOneInfo.title(screen, "Grapher Plotter", 20, 20)

        # Create instructions
        screenOneInfo.instructions(screen, "One square represents one unit.", 70)
        screenOneInfo.instructions(screen, "Press 'enter' when done or 'delete' to clear.", 100)
        screenOneInfo.instructions(screen, "Type an equation e.g. 2sin(x) - 3.", 130)

        ### Create shortcuts
        # 80px between shortcuts horizontally
        # Short
        screenOneInfo.shortcuts(screen, "s : ", 20, 1)
        screenOneInfo.shortcuts(screen, " c : ", 115, 1)
        screenOneInfo.shortcuts(screen, "  t : ", 210, 1)
        screenOneInfo.shortcuts(screen, "  r : ", 305, 1)
        screenOneInfo.shortcuts(screen, "a : ", 20, 2)
        screenOneInfo.shortcuts(screen, " l : ", 115, 2)
        screenOneInfo.shortcuts(screen, " n : ", 230, 2)
        screenOneInfo.shortcuts(screen, " e : ", 315, 2)
        screenOneInfo.shortcuts(screen, "p : ", 20, 3)
        screenOneInfo.shortcuts(screen, " q : ", 170, 3)
        screenOneInfo.shortcuts(screen, " w : ", 287, 3)
        screenOneInfo.shortcuts(screen, "y : ", 20, 4)
        screenOneInfo.shortcuts(screen, "^ : ", 135, 4)
        # Long
        screenOneInfo.shortcuts(screen, "sin() | ", 50, 1)
        screenOneInfo.shortcuts(screen, " cos() | ", 145, 1)
        screenOneInfo.shortcuts(screen, " tan() | ", 240, 1)
        screenOneInfo.shortcuts(screen, "sqrt()  ", 355, 1)
        screenOneInfo.shortcuts(screen, "abs() | ", 50, 2)
        screenOneInfo.shortcuts(screen, "log10() | ", 145, 2)
        screenOneInfo.shortcuts(screen, "ln() | ", 270, 2)
        screenOneInfo.shortcuts(screen, "e (~2.72) ", 350, 2)
        screenOneInfo.shortcuts(screen, "pi (~3.14) | ", 50, 3)
        screenOneInfo.shortcuts(screen, "sinh() | ", 210, 3)
        screenOneInfo.shortcuts(screen, "cosh()  ", 330, 3)
        screenOneInfo.shortcuts(screen, "tanh() | ", 50, 4)
        screenOneInfo.shortcuts(screen, "power | ", 170, 4)


        while True:
            # Constantly refresh the screen
            display.update()

            # Equation array refreshing
            buffer1 = 20
            screen.set_clip(buffer1, 180, self.extraWidth - 2* buffer1, 40)
            screen.fill(self.black)
            screen.set_clip(None)
            screen.set_clip(buffer1, 227, self.extraWidth - 2*buffer1, 40)
            screen.fill(self.black)
            screen.set_clip(None)

            ### Join strings to equation array without commas
            eq = "".join(equation)

            # Remove spaces
            eq = eq.replace(" ", "")

            # Render and blit equation
            showEqLabel = screenOneInfo.font6.render("Equation:", 1, self.yellow)
            screen.blit(showEqLabel, (30, 195))
            showEq = screenOneInfo.font4.render("y = " + eq, 1, self.white)
            screen.blit(showEq, (30, 232))

            # Prepare equation for the main processing algorithm in self.plotLine
            eq = eq.replace("^", "**")
            eq = eq.replace("ln(", "log(")
            eq = eq.replace("pix", "pi*x")
            for num in range(10):
                eq = eq.replace(str(num)+ "x", str(num) + "*x")
                eq = eq.replace(str(num)+ "sin(", str(num) + "*sin(")
                eq = eq.replace(str(num)+ "sinh(", str(num) + "*sinh(")
                eq = eq.replace(str(num)+ "cosh(", str(num) + "*cosh(")
                eq = eq.replace(str(num)+ "tanh(", str(num) + "tanh(")
                eq = eq.replace(str(num)+ "cos(", str(num) + "*cos(")
                eq = eq.replace(str(num)+ "tan(", str(num) + "*tan(")
                eq = eq.replace(str(num)+ "sqrt(", str(num) + "*sqrt(")
                eq = eq.replace(str(num)+ "abs(", str(num) + "*abs(")
                eq = eq.replace(str(num)+ "log10(", str(num) + "*log10(")
                eq = eq.replace(str(num)+ "log(", str(num) + "*log(")
                eq = eq.replace(str(num)+ "e", str(num) + "*e")
                eq = eq.replace(str(num)+ "pi", str(num) + "*pi")
                eq = eq.replace(str(num)+ "ex", str(num) + "e*x")

            # Check for any necessary events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # When a key is pressed, do something
                elif event.type == pygame.KEYDOWN:

                    if event.unicode == u'*':
                        equation.append("*")
                    elif event.unicode == u'+':
                        equation.append("+")
                    elif event.unicode == u'-':
                        equation.append("-")
                    elif event.unicode == u'/':
                        equation.append("/")
                    elif event.unicode == u'.':
                        equation.append(".")
                    elif event.unicode == u'(':
                        equation.append("(")
                    elif event.unicode == u')':
                        equation.append(")")
                    elif event.unicode == u'^':
                        equation.append("^")

                    elif event.key == K_1:
                        equation.append("1")
                    elif event.key == K_2:
                        equation.append("2")
                    elif event.key == K_3:
                        equation.append("3")
                    elif event.key == K_4:
                        equation.append("4")
                    elif event.key == K_5:
                        equation.append("5")
                    elif event.key == K_6:
                        equation.append("6")
                    elif event.key == K_7:
                        equation.append("7")
                    elif event.key == K_8:
                        equation.append("8")
                    elif event.key == K_9:
                        equation.append("9")
                    elif event.key == K_0:
                        equation.append("0")

                    # Math function commands    s c t r a l n e pi
                    elif event.key == K_s:
                        equation.append("sin(")
                    elif event.key == K_c:
                        equation.append("cos(")
                    elif event.key == K_q:
                        equation.append("sinh(")
                    elif event.key == K_t:
                        equation.append("tan(")
                    elif event.key == K_r:
                        equation.append("sqrt(")
                    elif event.key == K_a:
                        equation.append("abs(")
                    elif event.key == K_w:
                        equation.append("cosh(")
                    elif event.key == K_y:
                        equation.append("tanh(")
                    elif event.key == K_l:
                        equation.append("log10(")
                    elif event.key == K_n:
                        equation.append("ln(")
                    elif event.key == K_e:
                        equation.append("e")
                    elif event.key == K_p:
                        equation.append("pi")

                    elif event.key == K_x:
                        equation.append("x")
                    elif event.key == K_RETURN:
                        if len(equation) > 0:
                            # Amend eq where necessary to avoid an exception
                            if eq.count("(") > eq.count(")"):
                                count = eq.count("(") - eq.count(")")
                                eq += ")" * count

                            # Clip screen
                            screen.set_clip(0, 0, self.extraWidth, 0)
                            screen.fill(self.black)
                            screen.set_clip(0, 700, self.extraWidth, self.height - 00)
                            screen.fill(self.black)
                            screen.set_clip(None)

                            # Reset to correct colour
                            if Graphs == 1:
                                COLOUR = self.blue
                            if Graphs == 2:
                                COLOUR = self.orange
                            if Graphs == 3:
                                COLOUR = self.red
                            else:
                                COLOUR = self.lightBlue

                            # Plot the graph based on the equation input
                            self.plotLine(screen, k, eq, COLOUR)
                            self.presentScreenTwo(screen, k, eq, eq2)
                        break

                    elif event.key == K_DELETE:
                        equation = []
                        screen.fill(black)
                    elif event.key == K_BACKSPACE:
                        if len(equation) > 0:
                            del equation[-1]
                    elif event.key == K_g:
                        screen.fill(self.black)
                        GrapherMain(1, ' ')
        #sys.exit()

    def graphPaper(self, k, screen):
        # k is the number of pixels per unit on the grid
        screen.set_clip(self.extraWidth, 0, self.width, self.height)
        screen.fill(self.black)

        # Draw graph paper
        for i in range(int(self.width/k + 1)):
            if i != self.width/k:
                gridx = k * i
                gridy = k * i
            else:
                gridx = k * i - 1
                gridy = k * i - 1

            draw.line(screen, self.bizare, (self.extraWidth + gridx, 0),
                      (self.extraWidth + gridx, self.height), 1)
            draw.line(screen, self.bizare, (self.extraWidth, gridy),
                      (self.extraWidth + self.width, gridy), 1)

        # thick line between instructions and graph
        draw.line(screen, self.black, (self.extraWidth, 0),
                  (self.extraWidth, self.height), 5)

        # x and y axes
        midx = self.width/(2*k)
        midy = self.height/(2*k)

        # y axis
        draw.line(screen, self.lightGray, (self.extraWidth + midx*k , 0), (self.extraWidth + midx*k, self.height), 2)
        draw.line(screen, self.lightGray, (self.extraWidth + 0, 0), (self.extraWidth + 0, self.height), 2)
        draw.line(screen, self.lightGray, (self.extraWidth + midx*2*k, 0), (self.extraWidth + midx*2*k, self.height), 2)

        # x axis
        draw.line(screen, self.lightGray, (self.extraWidth, midy*k), (self.extraWidth + self.width, midy*k), 2)
   

        # Reset the clip on 'screen' to entire window
        screen.set_clip(None)

    def plotLine(self, screen, k, eq,COLOUR):

        # Graph the line, one pixel at a time
        for i in range(self.width):
            try:
                x = (self.width/2 - i)/float(k)
                y = eval(eq)
                pos1 = (self.width/2 + x * k + self.extraWidth, self.height/2 - y * k)

                nx = x = (self.width/2 - i - 1)/float(k)
                ny = eval(eq)
                pos2 = (self.width/2 + nx * k + self.extraWidth, self.height/2 - ny * k)

                BIG_NUM = 1000000000
              

                if (self.height/2 - y * k) - (self.height/2 - ny * k) > BIG_NUM:
                    # Asyptote so do not draw a line (vertical)
                    pass

                elif (self.height/2 - ny * k) - (self.height/2 - y * k) > BIG_NUM:
                    # Asyptote so do not draw a line (vertical)
                    pass
                else:
                    pygame.draw.line(screen, COLOUR, pos1, pos2, 2)
            except:
                # Add label for user feedback
                message = "INVALID EQUATION - Press enter, then type another equation."
                invalid = TextOnScreen.font5.render(message, 1, self.red)
                screen.blit(invalid, (20, 170))
                break

    def presentScreenTwo(self, screen, k, eq, eq2):
        screenTwoInfo = TextOnScreen()

        # Display info on second screen
        screen.set_clip(0, 0, self.extraWidth, 0)
        screen.fill(self.black)
        screenTwoInfo.instructions(screen, "Use '+' and '-' to change the size of the grid.", 40)
        screenTwoInfo.instructions(screen, "Press 'return' to draw another graph.", 70)
        if self.graph != 2:
            screenTwoInfo.instructions(screen, "Press 'backspace' to add a graph on a new layer.", 100)

        # Calculate y-intercept
        x = 0
        try:
            yInt = eval(eq)
            yInt = round(yInt, 2)
        except:
            yInt = 'dne'

        screenTwoInfo.instructions(screen, "The y-intercept is at (0," + str(yInt) + ").", 130)

        while True:

            # Update the screen
            display.update()

            # Keyboard and mouse actions - second screen
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                # When a key is pressed, do something
                elif event.type == pygame.KEYDOWN:

                    # Return replaces graph
                    if event.key == K_RETURN:
                        GrapherMain.graph = 1
                        newGrapherNext = GrapherMain(GrapherMain.graph, ' ')
                        self.graphPaper(k, screen)

                    # Backspace adds graph on a new layer
                    elif event.key == K_BACKSPACE and GrapherMain.graph == 1:
                        GrapherMain.graph = 2
                        newGrapherNext = GrapherMain(GrapherMain.graph, eq)

                    elif event.unicode == u'+' or event.unicode == u'=':
                        # next value in array kValues
                        if (self.kIndex >= len(self.kValues) - 1) == False:
                            self.kIndex += 1
                            k = self.kValues[self.kIndex]

                        # Refresh screen, fix jagged text bug
                        screen.set_clip(0, 0, self.extraWidth, 00)
                        screen.fill(self.black)
                        screen.set_clip(0, 700, self.extraWidth, self.height )
                        screen.fill(self.black)
                        screen.set_clip(None)

                        self.graphPaper(k, screen)

                        # Colour the graph based on the equation number (1 or 2)
                        if GrapherMain.graph == 1:
                            self.plotLine(screen, k, eq, self.blue)
                            self.presentScreenTwo(screen, k, eq, eq2)
                        elif GrapherMain.graph == 2:
                            self.plotLine(screen, k, eq, self.orange)
                            self.plotLine(screen, k, eq2, self.blue)
                            self.presentScreenTwo(screen, k, eq, eq2)

                    elif event.unicode == u'-':
                        # previous value in array kValues
                        if (self.kIndex <= 0) == False:
                            self.kIndex -= 1
                            k = self.kValues[self.kIndex]

                        # Refresh screen, fix jagged text bug
                        screen.set_clip(0, 0, self.extraWidth, 0)
                        screen.fill(self.black)
                        screen.set_clip(0, 700, self.extraWidth, self.height)
                        screen.fill(self.black)
                        screen.set_clip(None)

                        self.graphPaper(k, screen)

                        # Colour the graph based on the equation number (1 or 2)
                        if GrapherMain.graph == 1:
                            self.plotLine(screen, k, eq, self.blue)
                            self.presentScreenTwo(screen, k, eq, eq2)
                        elif GrapherMain.graph == 2:
                            self.plotLine(screen, k, eq, self.orange)
                            self.plotLine(screen, k, eq2, self.blue)
                            self.presentScreenTwo(screen, k, eq, eq2)

if __name__=='__main__':
    # Instantiate the main class (main program start point)
    initialGrapher = GrapherMain(GrapherMain.graph, ' ')
