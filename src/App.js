import React from 'react';
import { BrowserRouter, Switch, Route } from 'react-router-dom';

import Hompage from './pages/Hompage';
import Customers from './pages/Customers';
import Employees from './pages/Employees';
import Inventory from './pages/Inventory';
import Locations from './pages/Locations';
import Sales from './pages/Sales';

class App extends React.Component {
  render() {
    return (
      <BrowserRouter>
        <Switch>
          <Route exact path="/" component={Hompage} />
          <Route path="/locations" component={Locations} />
          <Route path="/employee" component={Employees} />
          <Route path="/inventory" component={Inventory} />
          <Route path="/sales" component={Sales} />
          <Route path="/customers" component={Customers} />
        </Switch>
      </BrowserRouter>
    );
  }
}

export default App;
