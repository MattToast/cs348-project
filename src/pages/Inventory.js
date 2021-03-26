import React from 'react';

import ObjectCard from '../components/ObjectCard/ObjectCard';
import NewInventoryForm from '../components/Forms/NewInventory';

class Inventory extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      inventoryList: []
    }
  }

  componentDidMount() {
    fetch('/api/inventory')
      .then(res => res.json())
      .then(data => this.setState({ inventoryList: data }));
  }

  render() {
    const inv = this.state.inventoryList;
    return (
      <div>
        <div>
          <NewInventoryForm />
        </div>
        <div>
          {
            inv.map((item) => {
              return (<ObjectCard data={item} />);
            })
          }
        </div>
      </div>
    );
  }
}

export default Inventory;
