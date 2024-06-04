import { Text, View } from "react-native";
import {store,persistor} from "./redux/store/store";
import { PersistGate } from 'redux-persist/integration/react';
import { Provider } from "react-redux";
import TodoApp from "./todoApp";

const App = () =>{
  return (
    <Provider store={store}>
    <PersistGate loading={null} persistor={persistor}>
      <TodoApp />
    </PersistGate>
  </Provider>
  )
}

export default App;