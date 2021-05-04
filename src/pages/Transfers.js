import React from 'react';

import NewTransferForm from '../components/Forms/NewTransferForm';
import ObjectCard from '../components/ObjectCard/ObjectCard';

class Transfers extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      transferList: []
    }
  }

  componentDidMount() {
    fetch('/api/transfers')
      .then(res => res.json())
      .then(data => this.setState({ transferList: data }));
  }

  render() {
    const trans = this.state.transferList;
    return (
      <div>
        <div>
          <NewTransferForm />
        </div>
        <div>
          {
            trans.map((tran) => {
              return (<ObjectCard data={tran} />);
            })
          }
        </div>
      </div>
    );
  }
}

export default Transfers;
