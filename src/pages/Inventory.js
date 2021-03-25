import React from 'react';

import ObjectCard from '../components/ObjectCard/ObjectCard';

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
        {
          inv.map((item) => {
            return (<ObjectCard data={item} />);
          })
        }
      </div>
    );
  }
}

export default Inventory;
