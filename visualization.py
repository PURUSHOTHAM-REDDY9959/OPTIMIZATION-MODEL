# Visualizing the results
products = ['Product A', 'Product B']
quantities = [x.varValue, y.varValue]

plt.bar(products, quantities, color=['skyblue', 'salmon'])
plt.title('Optimal Production Plan')
plt.ylabel('Units to Produce')
plt.grid(axis='y')
plt.show()