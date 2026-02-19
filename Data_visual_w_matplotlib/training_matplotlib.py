# from matplotlib import pyplot as plt

# x = [1, 2, 3, 4, 5]
# y = [1, 2, 3, 4, 5]

# plt.plot(x, y)

# plt.show


# import pandas as pd
# import matplotlib.pyplot as plt

# # 1. Load Data (assuming a DataFrame 'df_sales' is loaded)
# data = {'Month': ['Jan', 'Feb', 'Mar', 'Apr'], 'Revenue': [100, 150, 90, 200], 'Cost': [50, 70, 40, 60]}
# df_sales = pd.DataFrame(data)

# # 2. Create a Figure and Axes
# fig, ax = plt.subplots(figsize=(8, 5))

# # 3. Plotting the data
# ax.plot(df_sales['Month'], df_sales['Revenue'], marker='o', label='Revenue')
# ax.bar(df_sales['Month'], df_sales['Cost'], alpha=0.5, label='Cost')

# # 4. Customization
# ax.set_title('Monthly Revenue vs. Cost Analysis')
# ax.set_xlabel('Month')
# ax.set_ylabel('Amount (SEK)')
# ax.legend()
# plt.show()


#------------------------------------------------------

# import matplotlib.pyplot as plt

# # Create a Figure
# fig = plt.figure(figsize=(6,4))

# # Add Axes to the Figure
# ax = fig.add_subplot(111)  # 111 means "1x1 grid, first subplot"

# # Plot data
# ax.plot([1, 2, 3, 4, 10], [10, 20, 25, 30, 40])

# # Customize the Axis
# ax.set_xlim(0, 5)
# ax.set_ylim(0, 50)
# ax.set_xlabel('X Axis Label')
# ax.set_ylabel('Y Axis Label')
# ax.set_title('Sample Plot')

# # Show the plot
# plt.show()

#--------------------------------

# import matplotlib.pyplot as plt

# x = [0, 1, 2, 3, 4]
# y = [0, 1, 4, 9, 16]

# plt.plot(x, y)
# plt.show()


#----------------------------------------



# import matplotlib.pyplot as plt

# x = [0, 2, 4, 6, 8]
# y = [0, 4, 16, 36, 64]

# fig, ax = plt.subplots()

# ax.plot(x, y, marker="o", label= "Data point" )

# ax.set_title("Basic component of matplotlib")
# ax.set_xlabel("xaxis")
# ax.set_ylabel("yaxis")

# plt.show()


#--------------------------------

# # Python program to show pyplot module
# import matplotlib.pyplot as plt 
# from matplotlib.figure import Figure 

# # Creating a new figure with width = 5 inches and height = 4 inches
# fig = plt.figure(figsize =(5, 4)) 

# # Creating a new axes for the figure
# ax = fig.add_axes([0.1, 0.1, 0.8, 0.8]) 

# # Adding the data to be plotted
# ax.plot([2, 3, 4, 5, 5, 6, 6],
#         [5, 7, 1, 3, 4, 6 ,8])
# plt.show()

#------------------------------------


# Python program to show pyplot module
# import matplotlib.pyplot as plt 
# from matplotlib.figure import Figure 

# # Creating a new figure with width = 5 inches and height = 4 inches
# fig = plt.figure(figsize =(5, 4)) 

# # Creating first axes for the figure
# ax1 = fig.add_axes([1, 1, 1, 1]) 

# # Creating second axes for the figure
# ax2 = fig.add_axes([1, 0.5, 0.5, 0.5])

# # Adding the data to be plotted
# ax1.plot([2, 3, 4, 5, 5, 6, 6], 
#          [5, 7, 1, 3, 4, 6 ,8])
# ax2.plot([1, 2, 3, 4, 5], 
#          [2, 3, 4, 5, 6])

# plt.show()

#----------------------------------------


# import matplotlib.pyplot as plt 
# from matplotlib.figure import Figure 

# fig = plt.figure(figsize =(5, 4)) 

# # Adjusted coordinates to stay visible
# ax1 = fig.add_axes([0.1, 0.4, 0.6, 0.6])
# ax2 = fig.add_axes([0.1, 0.1, 0.3, 0.3])

# ax1.plot([2, 3, 4, 5, 5, 6, 6],
#          [5, 7, 1, 3, 4, 6 ,8])
# ax2.plot([1, 2, 3, 4, 5],
#          [2, 3, 4, 5, 6])

# plt.show()

