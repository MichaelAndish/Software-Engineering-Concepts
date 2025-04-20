### **StarBox Factory Method - TypeScript**

This code demonstrates the Factory Method pattern using a hypothetical **StarBox** coffee chain. The abstract class `StarBoxShop` defines the method `createStarBox()` for creating a `StarBox` drink, but leaves the actual implementation to its subclasses. Concrete classes like `CoffeeShop` and `LatteShop` implement this method to create specific drinks (`Coffee` and `Latte`). This approach allows the shop to handle drink preparation generically while providing platform-specific customization for different drink types.

---

### **Code**

```typescript
// 1. Interface for StarBox drinks
interface StarBox {
  serve(): void;
}

// 2. Concrete StarBox classes
class Coffee implements StarBox {
  serve() {
    console.log("Serving Coffee from StarBox!");
  }
}

class Latte implements StarBox {
  serve() {
    console.log("Serving Latte from StarBox!");
  }
}

// 3. Abstract class for StarBoxShop
abstract class StarBoxShop {
  protected abstract createStarBox(): StarBox;

  orderStarBox() {
    this.createStarBox().serve();
    console.log("Your StarBox drink is ready!");
  }
}

// 4. Concrete implementations for specific drinks
class CoffeeShop extends StarBoxShop {
  protected createStarBox(): Coffee {
    return new Coffee();
  }
}

class LatteShop extends StarBoxShop {
  protected createStarBox(): Latte {
    return new Latte();
  }
}

// 5. Using the Factory Method
const coffeeShop = new CoffeeShop();
coffeeShop.orderStarBox(); // Output: Serving Coffee from StarBox! Your StarBox drink is ready!

const latteShop = new LatteShop();
latteShop.orderStarBox(); // Output: Serving Latte from StarBox! Your StarBox drink is ready!
```

---

### **How It Works**

1. **Interface (`StarBox`)**:
   - Defines the structure for all drinks with a common `serve()` method.

2. **Concrete Classes**:
   - `Coffee` and `Latte` implement the `StarBox` interface and define how each drink is served.

3. **Abstract Class (`StarBoxShop`)**:
   - Declares the `createStarBox()` method, which is implemented by subclasses.
   - Handles the generic logic for ordering a drink (`orderStarBox()`).

4. **Concrete Implementations**:
   - `CoffeeShop` and `LatteShop` create specific drinks (e.g., Coffee or Latte).

5. **Usage**:
   - Create instances of specific shops (`CoffeeShop` or `LatteShop`) and call `orderStarBox()` to serve a drink.

---

### **Output**

```
Serving Coffee from StarBox!
Your StarBox drink is ready!
Serving Latte from StarBox!
Your StarBox drink is ready!
```

---

### **Advantages of Using Factory Method**

- **Flexibility**: Easily add new drink types (e.g., `EspressoShop`) without changing existing code.
- **Reusability**: Generic logic (`orderStarBox()`) is implemented once and reused across different subclasses.
- **Extensibility**: Add new drinks or shops by extending the `StarBox` interface and `StarBoxShop` class.

This design ensures scalability and maintainability for expanding the StarBox menu!