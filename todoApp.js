import React, { useState } from 'react';
import { View, Text, TextInput, Button, FlatList, StyleSheet } from 'react-native';
import { useSelector, useDispatch } from 'react-redux';
import { addTodo,removeTodo,editTodo } from './redux/actions'

const TodoApp = () => {
  const [text, setText] = useState('');
  const [isEditing, setIsEditing] = useState(false);
  const [currentIndex, setCurrentIndex] = useState(null);
  const todos = useSelector((state) => state.todos.todos);
  const dispatch = useDispatch();

  const handleAddTodo = () => {
    if (isEditing) {
      dispatch(editTodo(currentIndex, text));
      setIsEditing(false);
      setCurrentIndex(null);
    } else {
      dispatch(addTodo(text));
    }
    setText('');
  };

  const handleEditTodo = (index, todo) => {
    setText(todo);
    setIsEditing(true);
    setCurrentIndex(index);
  };

  const handleRemoveTodo = (index) => {
    dispatch(removeTodo(index));
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Todo List with Redux</Text>
      <TextInput
        style={styles.input}
        value={text}
        onChangeText={setText}
        placeholder="Enter todo"
      />
      <Button title={isEditing ? "Edit Todo" : "Add Todo"} onPress={handleAddTodo} />
      <FlatList
        data={todos}
        renderItem={({ item, index }) => (
          <View style={styles.todoItem}>
            <Text>{item}</Text>
            <Button title="Edit" onPress={() => handleEditTodo(index, item)} color={'orange'} />
            <Button title="Remove" onPress={() => handleRemoveTodo(index)} color={'red'} />
          </View>
        )}
        keyExtractor={(item, index) => index.toString()}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 16,
    backgroundColor: '#fff',
  },
  title: {
    fontSize: 24,
    marginBottom: 16,
  },
  input: {
    borderWidth: 1,
    borderColor: '#ccc',
    padding: 8,
    marginBottom: 16,
  },
  todoItem: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    padding: 8,
    borderBottomWidth: 1,
    borderBottomColor: '#ccc',
  },
});

export default TodoApp;

/********* above code without API */

// TodoApp.js
/***** below code when API's ARE there */
// import React, { useState, useEffect } from 'react';
// import { View, Text, TextInput, Button, FlatList, StyleSheet } from 'react-native';
// import { useSelector, useDispatch } from 'react-redux';
// import { fetchTodos, addTodo, removeTodo, editTodo } from './redux/actions/index';

// const TodoApp = () => {
//   const [text, setText] = useState('');
//   const [isEditing, setIsEditing] = useState(false);
//   const [currentId, setCurrentId] = useState(null);
//   const todos = useSelector((state) => state.todos.todos);
//   const dispatch = useDispatch();

//   useEffect(() => {
//     dispatch(fetchTodos());
//   }, [dispatch]);

//   const handleAddTodo = () => {
//     if (isEditing) {
//       dispatch(editTodo(currentId, text));
//       setIsEditing(false);
//       setCurrentId(null);
//     } else {
//       dispatch(addTodo(text));
//     }
//     setText('');
//   };

//   const handleEditTodo = (id, todo) => {
//     setText(todo);
//     setIsEditing(true);
//     setCurrentId(id);
//   };

//   const handleRemoveTodo = (id) => {
//     dispatch(removeTodo(id));
//   };

//   return (
//     <View style={styles.container}>
//       <Text style={styles.title}>Todo List</Text>
//       <TextInput
//         style={styles.input}
//         value={text}
//         onChangeText={setText}
//         placeholder="Enter todo"
//       />
//       <Button title={isEditing ? "Edit Todo" : "Add Todo"} onPress={handleAddTodo} />
//       <FlatList
//         data={todos}
//         renderItem={({ item }) => (
//           <View style={styles.todoItem}>
//             <Text>{item.text}</Text>
//             <Button title="Edit" onPress={() => handleEditTodo(item.id, item.text)} />
//             <Button title="Remove" onPress={() => handleRemoveTodo(item.id)} />
//           </View>
//         )}
//         keyExtractor={(item) => item.id.toString()}
//       />
//     </View>
//   );
// };

// const styles = StyleSheet.create({
//   container: {
//     flex: 1,
//     padding: 16,
//     backgroundColor: '#fff',
//   },
//   title: {
//     fontSize: 24,
//     marginBottom: 16,
//   },
//   input: {
//     borderWidth: 1,
//     borderColor: '#ccc',
//     padding: 8,
//     marginBottom: 16,
//   },
//   todoItem: {
//     flexDirection: 'row',
//     justifyContent: 'space-between',
//     padding: 8,
//     borderBottomWidth: 1,
//     borderBottomColor: '#ccc',
//   },
// });

// export default TodoApp;
