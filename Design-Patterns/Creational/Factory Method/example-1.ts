class Button{
    render(){
        console.log("Butting is rendered")
    }
}


class ButtonIOS extends Button{
    render(){
        console.log("IOS Button is rendered")
    }    
}

class ButtonAndroid extends Button{
    render(){
        console.log("Android Button is rendered")
    }    
}


abstract class App{
    abstract createButton(): Button

    render(){
       this.createButton().render()
       console.log("App is rendered")     
    }
}

class AppIOS extends App{
    createButton(): Button {
        return new ButtonIOS();
    }
}

class AppAndroid extends App{
    createButton(): Button {
        return new ButtonAndroid();
    }
}



