

from msilib.schema import CheckBox
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog

# Main Screen Setup

root = tk.Tk()
root.geometry('1300x650+0+0')  # Length by width, x position + y position
root.resizable(False, False)  # X direction and y direction (0,1 works too)
root.title('The Incredible Spice: Invoicing System')

img = (
  Image.open('C:\\Users\\soham\\Desktop\\Tkinter-Modified\\background.jpg'))
resized = img.resize((1300, 650))
newimg = ImageTk.PhotoImage(resized)
#root.config(image=img)
root.config(bg='#3a5311')

# Background

label = Label(root, image=newimg)
label.place(x=0, y=0)

# Top Panel

topPanel = Frame(
  root, bd=1, relief=RAISED
)  # Container to organise widgets, relief can be raised, sunken, groove, ridge, flat
topPanel.pack(side=TOP)
top_title = Label(topPanel,
                  text='The Incredible Spice',
                  fg='#ffd700',
                  font=('Dosis', 58),
                  bg='#234f1e',
                  width=25)  # fg = foreground
top_title.grid(row=0, column=0)

# Left Panel (with food, drinks, dessert and cost)

leftPanel = Frame(root, bd=1, relief=RAISED, bg='black')
leftPanel.place(relx=0.05, rely=0.15)

# Cost Panel

costPanel = Frame(leftPanel, bd=1, relief=FLAT, bg='black', padx=50)
costPanel.pack(side=BOTTOM)

submitPanel = Frame(leftPanel, bd=1, relief=RAISED, bg='black')
submitPanel.pack(side=BOTTOM)

# Food Panel

foodPanel = LabelFrame(leftPanel,
                       bd=1,
                       relief=FLAT,
                       text='Food',
                       fg='#2e1503',
                       font=('Dosis', 22, 'bold', 'underline'),
                       bg='#74b72e')
foodPanel.pack(side=LEFT)

# Drink Panel

drinkPanel = LabelFrame(leftPanel,
                        bd=1,
                        relief=FLAT,
                        text='Drinks',
                        fg='#2e1503',
                        font=('Dosis', 22, 'bold', 'underline'),
                        padx=10,
                        bg='#74b72e')
drinkPanel.pack(side=LEFT)

# Dessert Panel

dessertPanel = LabelFrame(leftPanel,
                          bd=1,
                          relief=FLAT,
                          text='Dessert',
                          fg='#2e1503',
                          font=('Dosis', 22, 'bold', 'underline'),
                          padx=10,
                          bg='#74b72e')
dessertPanel.pack(side=LEFT)

'''# Right Panel

rightPanel = Frame(root, bd=1, relief=RAISED, bg='black')
rightPanel.pack(side=LEFT)

# Calculator

calculatorOutput = Frame(rightPanel, bd=1, relief=RAISED, bg='black')
calculatorOutput.pack()

calculator = Frame(rightPanel, bd=1, relief=RAISED, bg='black')
calculator.pack()  # Top by default




# Invoice Panel



invoicePanel = Frame(rightPanel, bd=1, relief=FLAT, bg='burlywood')
invoicePanel.pack()

# Buttons

buttonPanel = Frame(rightPanel, bd=1, relief=FLAT, bg='burlywood')
buttonPanel.pack()  # Specify only from left to right'''

# Back-End Stuff


foods = [
  'Lazeez Biriyani', 'Paneer Roll', 'Fried Lettuce', 'Boiled Ice Cream',
  'Khuska', 'Kebabs', 'Fried Rice', 'Cinnamon Toast'
]
foodCosts = [350, 80, 150, 130, 100, 450, 180, 70]
drinks = [
  'Juice', 'Lemonade', 'Soda', 'Ginger ale', 'Coke', 'Liquid Cake',
  'Milkshake', 'Water'
]
drinkCosts = [50, 70, 80, 80, 50, 100, 20, 20]
desserts = [
  'Dragonfruit Curd', 'Paneer Milk', 'Sugared Almonds', 'Cheesecake',
  'Brownies', 'Pudding', 'Candyfloss', 'Pie'
]
dessertCosts = [175, 75, 225, 250, 180, 120, 5, 250]

food_cost_var = StringVar()
drink_cost_var = StringVar()
dessert_cost_var = StringVar()
subtotal_cost_var = StringVar()
taxes_var = StringVar()
total_var = StringVar()

# Check boxes

# Creating food items

counter = 0
food_variables = []
foodBox = []
foodText = []


def checkFoodClicked():
  for i in range(len(food_variables)):
    if food_variables[i].get() == 1:
      foodBox[i].configure(state=NORMAL)
    else:
      foodText[i].set('0')
      food_variables[i].set(0)
      foodBox[i].configure(state=DISABLED)
      
invoiceTextVar = StringVar()
totalStuff="Item - Quantity - Total Cost \n \n"

foodCost=0
drinkCost=0
dessertCost=0

expression=""
equation=StringVar()
def addEverything():
    global invoiceTextVar
    global totalStuff
    global foodCost
    global drinkCost
    global dessertCost

    for i in range(len(foodText)):
        foodCost+=int(foodText[i].get())*foodCosts[i]
    for j in range(len(drinkText)):
        drinkCost+=int(drinkText[j].get())*foodCosts[j]
    for k in range(len(dessertText)):
        dessertCost+=int(dessertText[k].get())*foodCosts[k]
    food_cost_var.set(str(foodCost))
    drink_cost_var.set(str(drinkCost))
    dessert_cost_var.set(str(dessertCost))
    subtotal_cost_var.set(str(foodCost+drinkCost+dessertCost))
    taxes_var.set(str((foodCost+drinkCost+dessertCost)/10))
    total_var.set(str(int(1.1*(foodCost+drinkCost+dessertCost))))
    for i in range(len(foodText)):
      if int(foodText[i].get())!=0:
        #print(foods[i], foodText[i].get(), int(foodText[i].get())*foodCosts[i], sep = " - ")
        totalStuff+=str(str(foods[i]) + " - " + str(foodText[i].get()) + " - " + str(int(foodText[i].get())*foodCosts[i]))
        totalStuff+="\n"
    for i in range(len(drinkText)):
      if int(drinkText[i].get())!=0:
        #print(foods[i], foodText[i].get(), int(foodText[i].get())*foodCosts[i], sep = " - ")
        totalStuff+=str(str(drinks[i]) + " - " + str(drinkText[i].get()) + " - " + str(int(drinkText[i].get())*drinkCosts[i]))
        totalStuff+="\n"
    for i in range(len(dessertText)):
      if int(dessertText[i].get())!=0:
        #print(foods[i], foodText[i].get(), int(foodText[i].get())*foodCosts[i], sep = " - ")
        totalStuff+=str(str(desserts[i]) + " - " + str(dessertText[i].get()) + " - " + str(int(dessertText[i].get())*dessertCosts[i]))
        totalStuff+="\n"
    totalStuff+="\n **************************** \n"
    totalStuff+=str(str("Subtotal ") + str(" - ") + str(foodCost+drinkCost+dessertCost) + str("\n"))
    totalStuff+=str(str("Total ") + str(" - ") + str(int(1.1*(foodCost+drinkCost+dessertCost))) + str("\n"))
    totalStuff+=str("Thank you!")
    invoiceTextVar.set(totalStuff)
    global billingScreen
    billingScreen = tk.Tk()
    billingScreen.config(bg='black')
    billingScreen.geometry('500x600+0+0')
    billingScreen.title('Invoice')
    billingScreen.resizable(False, False)

    # Right Panel
    rightPanel = Frame(billingScreen, bd=1, relief=RAISED, bg='black')
    rightPanel.pack(side=LEFT)

    # Calculator

    calculatorOutput = Frame(billingScreen, bd=1, relief=RAISED, bg='black')
    calculatorOutput.pack()

    calculator = Frame(billingScreen, bd=1, relief=RAISED, bg='black')
    calculator.pack()  # Top by default
    
    titleLabel = Label(calculatorOutput, text="Calculator and Invoice", font=('Dosis', 19, 'bold', 'underline'), fg='black', bg='green', relief=FLAT)
    titleLabel.pack()  
    box = Label(calculatorOutput, text=equation.get(), width=50, state=NORMAL, font=('Dosis', 12))
    box.pack()

    def press(val):
        global expression
        expression+=str(val)
        equation.set(expression)
        box.config(text=expression)

    def equate():
        try:
            expression = (eval(equation.get()))
            box.config(text=expression)
        except:
            equation.set("error")
            expression=""

    def clear():
        global expression
        equation.set("")
        expression = ""
        box.config(text=expression)
        


    button1 = Button(calculator, bg = '#03ac13', fg='black', text='1', width=15, height=2, command=lambda: press(1))
    button1.grid(row=1, column=0)
    button2 = Button(calculator, bg = '#03ac13', fg='black', text='2', width=15, height=2, command=lambda: press(2))
    button2.grid(row=1, column=1)
    button3 = Button(calculator, bg = '#03ac13', fg='black', text='3', width=15, height=2, command=lambda: press(3))
    button3.grid(row=1, column=2)
    button4 = Button(calculator, bg = '#03ac13', fg='black', text='4', width=15, height=2, command=lambda: press(4))
    button4.grid(row=1, column=3)
    button5 = Button(calculator, bg = '#03ac13', fg='black', text='5', width=15, height=2, command=lambda: press(5))
    button5.grid(row=2, column=0)
    button6 = Button(calculator, bg = '#03ac13', fg='black', text='6', width=15, height=2, command=lambda: press(6))
    button6.grid(row=2, column=1)
    button7 = Button(calculator, bg = '#03ac13', fg='black', text='7', width=15, height=2, command=lambda: press(7))
    button7.grid(row=2, column=2)
    button8 = Button(calculator, bg = '#03ac13', fg='black', text='8', width=15, height=2, command=lambda: press(8))
    button8.grid(row=2, column=3)
    button9 = Button(calculator, bg = '#03ac13', fg='black', text='9', width=15, height=2, command=lambda: press(9))
    button9.grid(row=3, column=0)
    button0 = Button(calculator, bg = '#03ac13', fg='black', text='0', width=15, height=2, command=lambda: press(0))
    button0.grid(row=3, column=1)

    add = Button(calculator, bg = '#03ac13', fg='black', text='+', width=15, height=2, command=lambda: press('+'))
    add.grid(row=3, column=2)
    subtract = Button(calculator, bg = '#03ac13', fg='black', text='-', width=15, height=2, command=lambda: press('-'))
    subtract.grid(row=3, column=3)
    multiply = Button(calculator, bg = '#03ac13', fg='black', text='x', width=15, height=2, command=lambda: press('*'))
    multiply.grid(row=4, column=0)
    divide = Button(calculator, bg = '#03ac13', fg='black', text='/', width=15, height=2, command=lambda: press('/'))
    divide.grid(row=4, column=1)
    equal = Button(calculator, bg = '#03ac13', fg='black', text='=', width=15, height=2, command=equate)
    equal.grid(row=4, column=2)
    clear = Button(calculator, bg = '#03ac13', fg='black', text='clear', width=15, height=2, command=clear)
    clear.grid(row=4, column=3)
    
        # Put this back
    invoicePanel = Frame(billingScreen, bd=1, relief=FLAT, bg='burlywood')
    invoicePanel.pack()

    # Buttons

    buttonPanel = Frame(billingScreen, bd=1, relief=FLAT, bg='burlywood')
    buttonPanel.pack()  # Specify only from left to right

    saveButton = Button(buttonPanel,
                        text='Save',
                        relief=RAISED,
                        font=('Dosis', 19, 'bold'),
                        fg='black',
                        bg='green',
                        bd=1,
                        width=8,
                        command=createFile)
    saveButton.grid(row=0, column=0)

    clearButton = Button(buttonPanel,
                            text='Clear',
                            relief=RAISED,
                            font=('Dosis', 19, 'bold'),
                            fg='black',
                            bg='green',
                            bd=1,
                            width=8,
                            command=clearAll)
    clearButton.grid(row=0, column=1)

    invoiceText = LabelFrame(invoicePanel, width=450, height=275, font=('Dosis', 10, 'bold'), text="Invoice - The Incredible Spice")
    invoiceText.pack()
    global invoiceLabel
    invoiceLabel = Label(invoiceText, width=50, height=15, font=('Dosis', 10, 'bold'))
    invoiceLabel.pack(expand=True, fill='both')
    invoiceLabel.configure(text=invoiceTextVar.get())
    billingScreen.protocol("WM_DELETE_WINDOW", clearAll)
    billingScreen.mainloop()




def clearAll():
  global totalStuff
  global invoiceTextVar
  global billingScreen
  totalStuff=""
  invoiceTextVar.set("")
  global invoiceLabel
  invoiceLabel.configure(text=invoiceTextVar.get())
  global foodCost
  foodCost=0
  global drinkCost
  drinkCost=0
  global dessertCost
  dessertCost=0
  food_cost_var.set(" ")
  drink_cost_var.set(" ")
  dessert_cost_var.set(" ")
  subtotal_cost_var.set(" ")
  taxes_var.set(" ")
  total_var.set(" ")
  billingScreen.destroy()
  
  
  for i in range(len(dessert_variables)):
    dessertText[i].set('0')
    dessert_variables[i].set(0)
    dessertBox[i].config(state=DISABLED)
    
  for j in range(len(food_variables)):
    foodText[j].set('0')
    food_variables[j].set(0)
    foodBox[j].config(state=DISABLED)
    
  for k in range(len(drink_variables)):
    drinkText[k].set('0')
    drink_variables[k].set(0)
    drinkBox[k].config(state=DISABLED)
    


for food in foods:
  food_variables.append('')
  food_variables[counter] = IntVar(
  )  # Creates an integer variable (type-casting)
  food = Checkbutton(
    foodPanel,
    text=str(food.title() + " - " + str(foodCosts[foods.index(food)])),
    font=('Dosis', 19, 'bold'),
    onvalue=1,
    offvalue=0,
    variable=food_variables[counter],
    bg='#74b72e',
    command=checkFoodClicked
  )  # Every element becomes a check button; when checked, check's value is 1 else 0
  # Creates a variable (checkbox) for every item
  food.grid(row=counter, column=0, sticky=W)  # West
  # Creating input boxes (no. of items), food box is a list which stores the food input boxes, food text stores the text in those boxes
  foodBox.append('')
  foodText.append('')
  foodText[counter] = StringVar()
  foodText[counter].set('0')  # When using the value, use an integer, when entering, use a string
  foodBox[counter] = Entry(
    foodPanel,
    bd=1,
    font=('Dosis', 19, 'bold'),
    width=6,
    state=DISABLED,
    textvariable=foodText[counter],
  )  # Until checking the checkbox, the input is disabled
  foodBox[counter].grid(row=counter, column=1)
  counter += 1

# Creating drink items

counter = 0
drink_variables = []
drinkBox = []
drinkText = []


def checkDrinkClicked():
  for i in range(len(drink_variables)):
    if drink_variables[i].get() == 1:
      drinkBox[i].config(state=NORMAL)
    else:
      drinkText[i].set('0')
      drink_variables[i].set(0)
      drinkBox[i].config(state=DISABLED)


for drink in drinks:
  drink_variables.append('')
  drink_variables[counter] = IntVar(
  )  # Creates an integer variable (type-casting)
  drink = Checkbutton(
    drinkPanel,
    text=str(drink.title() + " - " + str(drinkCosts[drinks.index(drink)])),
    font=('Dosis', 19, 'bold'),
    onvalue=1,
    offvalue=0,
    variable=drink_variables[counter],
    bg='#74b72e',
    command=checkDrinkClicked
  )  # Every element becomes a check button; when checked, check's value is 1 else 0
  # Creates a variable (checkbox) for every item
  drink.grid(row=counter, column=0, sticky=W)  # West
  # Creating input boxes (no. of items), food box is a list which stores the food input boxes, food text stores the text in those boxes
  drinkBox.append('')
  drinkText.append('')
  drinkText[counter] = StringVar()
  drinkText[counter].set('0')
  drinkBox[counter] = Entry(
    drinkPanel,
    bd=1,
    font=('Dosis', 19, 'bold'),
    width=6,
    state=DISABLED,
    textvariable=drinkText[counter]
  )  # Until checking the checkbox, the input is disabled
  drinkBox[counter].grid(row=counter, column=1)
  counter += 1

# Creating dessert items

counter = 0
dessert_variables = []
dessertBox = []
dessertText = []


def checkDessertClicked():
  for i in range(len(dessert_variables)):
    if dessert_variables[i].get() == 1:
      dessertBox[i].config(state=NORMAL)
    else:
      dessertText[i].set('0')
      dessert_variables[i].set(0)
      dessertBox[i].config(state=DISABLED)


for dessert in desserts:
  dessert_variables.append(
    'placeholder'
  )  # All the placeholders are going to be changed later, these are checkboxes
  dessert_variables[counter] = IntVar(
  )  # Creates an integer variable (type-casting)
  dessert = Checkbutton(
    dessertPanel,
    text=str(dessert.title() + " - " + str(dessertCosts[desserts.index(dessert)])),
    font=('Dosis', 19, 'bold'),
    onvalue=1,
    offvalue=0,
    variable=dessert_variables[counter],
    bg='#74b72e',
    command=checkDessertClicked
  )  # Every element becomes a check button; when checked, check's value is 1 else 0
  # Creates a variable (checkbox) for every item
  dessert.grid(row=counter, column=0, sticky=W)  # West
  # Creating input boxes (no. of items), food box is a list which stores the food input boxes, food text stores the text in those boxes
  dessertBox.append('')
  dessertText.append('')
  dessertText[counter] = StringVar()
  dessertText[counter].set('0')
  dessertBox[counter] = Entry(
    dessertPanel,
    bd=1,
    font=('Dosis', 19, 'bold'),
    width=6,
    state=DISABLED,
    textvariable=dessertText[counter]
  )  # Until checking the checkbox, the input is disabled
  dessertBox[counter].grid(row=counter, column=1)
  counter += 1
  
submitButton = Button(submitPanel, width = 20, height=1, bg='green', text='Submit', font = ('Dosis', 19, 'bold'), command=addEverything)
submitButton.grid(row = 0, column = 1)


food_cost_label = Label(costPanel,
                        text='Food Costs',
                        font=('Dosis', 12, 'bold'),
                        bg='black',
                        fg='#ffd700')
food_cost_label.grid(row=1, column=0)
food_cost_text = Entry(costPanel,
                       font=('Dosis', 12, 'bold'),
                       bd=1,
                       width=10,
                       state='readonly',
                       textvariable=food_cost_var)
food_cost_text.grid(row=1, column=1, padx=60)

drink_cost_label = Label(costPanel,
                         text='Drink Costs',
                         font=('Dosis', 12, 'bold'),
                         fg='#ffd700',
                         bg='black')
drink_cost_label.grid(row=2, column=0)
drink_cost_text = Entry(costPanel,
                        font=('Dosis', 12, 'bold'),
                        bd=1,
                        width=10,
                        state='readonly',
                        textvariable=drink_cost_var)
drink_cost_text.grid(row=2, column=1)

dessert_cost_label = Label(costPanel,
                           text='Dessert Costs',
                           font=('Dosis', 12, 'bold'),
                           fg='#ffd700',
                           bg='black')
dessert_cost_label.grid(row=3, column=0)
dessert_cost_text = Entry(costPanel,
                          font=('Dosis', 12, 'bold'),
                          bd=1,
                          width=10,
                          state='readonly',
                          textvariable=dessert_cost_var)
dessert_cost_text.grid(row=3, column=1)

subtotal_cost_label = Label(costPanel,
                            text='Subtotal',
                            font=('Dosis', 12, 'bold'),
                            fg='#ffd700',
                            bg='black')
subtotal_cost_label.grid(row=1, column=2, padx=60)
subtotal_cost_text = Entry(costPanel,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=subtotal_cost_var)
subtotal_cost_text.grid(row=1, column=3)


def createFile():
    text_file = filedialog.asksaveasfile(mode='w', initialdir='C://Users//soham//Desktop', title='Save As', filetypes=[("text", "*.txt"), ("pdf", "*.pdf"), ("png", "*.png")])
    text_file.write(totalStuff)

taxes_cost_label = Label(costPanel,
                         text='Taxes',
                         font=('Dosis', 12, 'bold'),
                         fg='#ffd700',
                         bg='black')
taxes_cost_label.grid(row=2, column=2)
taxes_cost_text = Entry(costPanel,
                        font=('Dosis', 12, 'bold'),
                        bd=1,
                        width=10,
                        state='readonly',
                        textvariable=taxes_var)
taxes_cost_text.grid(row=2, column=3)

total_cost_label = Label(costPanel,
                         text='Total',
                         font=('Dosis', 12, 'bold'),
                         fg='#ffd700',
                         bg='black')
total_cost_label.grid(row=3, column=2)
total_cost_text = Entry(costPanel,
                        font=('Dosis', 12, 'bold'),
                        bd=1,
                        width=10,
                        state='readonly',
                        textvariable = total_var)
total_cost_text.grid(row=3, column=3)


                                                                                                                                             
root.mainloop()





