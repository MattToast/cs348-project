import React from 'react';

import NewSaleForm from '../components/Forms/NewSaleForm.js';
import PartyImg from '../img/party.png';

class SuccessfulSale extends React.Component {
  constructor(props) {
    super(props);
    this.state = {};
  }

  render() {
    return (
      <div>
        <h1>Congrats Employee, Sale Made!!</h1>
        <NewSaleForm />
        <div>
          <img src={PartyImg} alt="Party Emoji" width="250"/>
          <img src={PartyImg} alt="Party Emoji" width="250"/>
          <img src={PartyImg} alt="Party Emoji" width="250"/>
        </div>
      </div>
    );
  }
}

export default SuccessfulSale;