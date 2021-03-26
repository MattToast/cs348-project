import React from 'react';

import ObjectCard from '../components/ObjectCard/ObjectCard';

class Buy extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      buyList: []
    }
  }

  componentDidMount() {
    fetch('/api/buys')
      .then(res => res.json())
      .then(data => this.setState({ buyList: data }));
  }

  render() {
    const buys = this.state.buyList;
    return (
      <div>
        <div>
          TODO - Adding should be handled automatically by the made sale page
        </div>
        <div>
          {
            buys.map((buy) => {
              return (<ObjectCard data={buy} />);
            })
          }
        </div>
      </div>
    );
  }
}

export default Buy;
