/** 
 * Create a class called ShoppingCart.

 * Create a constructor that has no arguments and sets the total attribute to zero, and initializes an empty dict attribute named items.

 * Create a method add_item that requires item_name, quantity and price arguments. This method should add the cost of the added items to the current value of total. It should also add an entry to the items dict such that the key is the item_name and the value is the quantity of the item.

 * Create a method remove_item that requires similar arguments as add_item. It should remove items that have been added to the shopping cart and are not required. This method should deduct the cost of these items from the current total and also update the items dict accordingly. If the quantity of items to be removed exceeds current quantity in cart, assume that all entries of that item are to be removed.

 * Create a method checkout that takes in cash_paid and returns the value of balance from the payment. If cash_paid is not enough to cover the total, return Cash paid not enough.

 * Create a class called Shop that has a constructor which initializes an attribute called quantity at 100.

 * Make sure Shop inherits from ShoppingCart.

 * In the Shop class, override the remove_item method, such that calling Shop's remove_item with no arguments decrements quantity by one.
 */

function ShoppingCart() {
  this.total = 0;
  this.items = {};
}

ShoppingCart.prototype.addItem = function(itemName, quantity, price) {
  this.total += price * quantity;
  this.items[itemName] = quantity;
};

ShoppingCart.prototype.removeItem = function(itemName, quantity, price) {
  this.total -= price * quantity;
  this.items[itemName] = this.items[itemName] - quantity;
};

ShoppingCart.prototype.checkout = function(cashPaid) {
  if (cashPaid < this.total) {
    return 'Cash paid not enough';
  }
  return cashPaid - this.total;
};

function Shop() {
  this.quantity = 100;
}

Shop.prototype = Object.create(ShoppingCart.prototype);

Shop.prototype.removeItem = function() {
  this.quantity = this.quantity - 1;
};
