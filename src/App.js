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
          <Route path="/customers" component={Customers} />
          <Route path="/employees" component={Employees} />
          <Route path="/inventory" component={Inventory} />
          <Route path="/locations" component={Locations} />
          <Route path="/sales" component={Sales} />
        </Switch>
      </BrowserRouter>
    );
  }
}

export default App;
