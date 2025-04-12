# Cross-platform App Example - TypeScript

This code demonstrates the Factory Method pattern, where the abstract class `App` defines a method `createButton()` to create a `Button`, but leaves the actual button creation to its subclasses. `AppIOS` and `AppAndroid` each implement this method to return platform-specific buttons (`ButtonIOS` and `ButtonAndroid`). This allows the `App` class to use the created button without knowing its exact type, enabling flexibility and platform-specific customization while keeping the rendering logic (render) consistent and reusable.

```ts
interface Button {
  render: () => void;
}

class ButtonIOS implements Button {
  render() {
    console.log("IOS Button is rendered");
  }
}

class ButtonAndroid implements Button {
  render() {
    console.log("Android Button is rendered");
  }
}

abstract class App {
  protected abstract createButton(): Button;

  render() {
    this.createButton().render();
    console.log("App is rendered");
  }
}

class AppIOS extends App {
  createButton(): ButtonIOS {
    return new ButtonIOS();
  }
}

class AppAndroid extends App {
  createButton(): ButtonAndroid {
    return new ButtonAndroid();
  }
}
```
