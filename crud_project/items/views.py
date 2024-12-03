from django.shortcuts import render, redirect
from .models import Item

# Read: List all items
def item_list(request):
    items = Item.objects.all()
    return render(request, 'items/item_list.html', {'items': items})

# Create: Add a new item
def create_item(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        price = request.POST['price']
        Item.objects.create(name=name, description=description, price=price)
        return redirect('item_list')
    return render(request, 'items/create_item.html')

# Update: Edit an existing item
def update_item(request, pk):
    item = Item.objects.get(id=pk)
    if request.method == 'POST':
        item.name = request.POST['name']
        item.description = request.POST['description']
        item.price = request.POST['price']
        item.save()
        return redirect('item_list')
    return render(request, 'items/update_item.html', {'item': item})

# Delete: Remove an item
def delete_item(request, pk):
    item = Item.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('item_list')
    return render(request, 'items/delete_item.html', {'item': item})
