import React from "react";
import './App.css';
// import * as RBS from "react-bootstrap";
import Button from 'react-bootstrap/Button';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Form from 'react-bootstrap/Form';
import Modal from 'react-bootstrap/Modal';
import Navbar from 'react-bootstrap/Navbar';
import Nav from 'react-bootstrap/Nav';
import Card from 'react-bootstrap/Card';
import Container from 'react-bootstrap/Container';
import Carousel from 'react-bootstrap/Carousel';
function App() {
  const [modalShowIn, setModalShowSignIn] = React.useState(false);
  const [modalShowUp, setModalShowSignUp] = React.useState(false);
  return (

    <div className="App">
      <row>
        <div className="NavBar">
        <Navbar collapseOnSelect expand="lg" bg="primary" variant="dark" className="p-4">

          <Navbar.Brand href="#home" className="display 1">ONTOGENESIS</Navbar.Brand>
          <Navbar.Toggle aria-controls="responsive-navbar-nav" />
          <Navbar.Collapse id="responsive-navbar-nav">
            <Nav className="me-auto" className="ms-auto">
              <Nav.Link href="#deets">
                Dashboard
              </Nav.Link>
              <Nav.Link href="#memes">
                Log Out            
              </Nav.Link>
            </Nav>
          </Navbar.Collapse>
          
        </Navbar>
        </div>
      </row>
      <row>
        <div className="Carousel">
          <Carousel>
            <Carousel.Item interval={1000}>
              <img
                className="d-block w-100"
                // src="HealthCare"
                alt="First slide"
              />
              {/* <Carousel.Caption>
                <h3>First slide label</h3>
                <p>Nulla vitae elit libero, a pharetra augue mollis interdum.</p>
              </Carousel.Caption> */}
            </Carousel.Item>
            <Carousel.Item interval={500}>
              <img
                className="d-block w-100"
                src="holder.js/800x400?text=Second slide&bg=282c34"
                alt="Second slide"
              />
              {/* <Carousel.Caption>
                <h3>Second slide label</h3>
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
              </Carousel.Caption> */}
            </Carousel.Item>
            <Carousel.Item>
              <img
                className="d-block w-100"
                src="holder.js/800x400?text=Third slide&bg=20232a"
                alt="Third slide"
              />
              {/* <Carousel.Caption>
                <h3>Third slide label</h3>
                <p>Praesent commodo cursus magna, vel scelerisque nisl consectetur.</p>
              </Carousel.Caption> */}
            </Carousel.Item>
          </Carousel>
        </div>
      </row>
      <row>
        <div className="Content">
        <Card> 
          <Card.Header as="h4">What is ontogenesis ?</Card.Header>
          <Card.Body>
            <Card.Text>
              It is a cloud based web application that maintains patient's clinical and prescription data enabling authorities to manage resources for disease outbreaks.
            </Card.Text>
            <Card.Text>
              It maintains patient's clinical and prescription data.
            </Card.Text>
            <Container>
              <Row>
                <Col>
                  <Button variant="primary" onClick={() => setModalShowSignIn(true)}>
                    Sign In
                  </Button>
                </Col>
                <Col>
                  <Button variant="primary" onClick={() => setModalShowSignUp(true)}>
                    Sign Up
                  </Button>    
                </Col>
              </Row>
            </Container>
            <ModalShowIn
              show={modalShowIn}
              onHide={() => setModalShowSignIn(false)}
            />
            <ModalShowUp
              show={modalShowUp}
              
              onHide={() => setModalShowSignUp(false)}
            />
          </Card.Body>
        </Card>
        </div>
      </row>
    </div>
  );
}

function ModalShowIn(props) {
  return (
    <Modal
      {...props}
      size="lg"
      aria-labelledby="contained-modal-title-vcenter"
      centered
    >
      <Modal.Header closeButton>
        <Modal.Title id="contained-modal-title-vcenter">
          Sign In
        </Modal.Title>
      </Modal.Header>
      <Modal.Body>
        <Form>
          <Form.Group className="mb-3" controlId="formBasicEmail">
            <Form.Label>Email address</Form.Label>
            <Form.Control type="email" placeholder="Enter email" />
          </Form.Group>

          <Form.Group className="mb-3" controlId="formBasicPassword">
            <Form.Label>Password</Form.Label>
            <Form.Control type="password" placeholder="Password" />
          </Form.Group>
          <Button variant="primary" type="submit">
            Submit
          </Button>
        </Form>
      </Modal.Body>
      <Modal.Footer>
        <Button onClick={props.onHide}>Close</Button>
      </Modal.Footer>
    </Modal>
  );
}

function ModalShowUp(props) {
  return (
    <Modal
      {...props}
      size="lg"
      aria-labelledby="contained-modal-title-vcenter"
      centered
    >
      <Modal.Header closeButton>
        <Modal.Title id="contained-modal-title-vcenter">
          Sign In
        </Modal.Title>
      </Modal.Header>
      <Modal.Body>
        <Form>
          <Row className="mb-3">
            <Form.Group as={Col} controlId="formGridFirstName">
              <Form.Label>First Name</Form.Label>
              <Form.Control type="text" placeholder="Enter First Name" />
            </Form.Group>

            <Form.Group as={Col} controlId="formGridLastName">
              <Form.Label>Last Name</Form.Label>
              <Form.Control type="text" placeholder="Enter Last Name" />
            </Form.Group>
          </Row>
          <Row className="mb-3">
            <Form.Group as={Col} controlId="formGridEmail">
              <Form.Label>Email</Form.Label>
              <Form.Control type="email" placeholder="Enter email" />
            </Form.Group>

            <Form.Group as={Col} controlId="formGridPassword">
              <Form.Label>Password</Form.Label>
              <Form.Control type="password" placeholder="Password" />
            </Form.Group>
          </Row>

          <Form.Group className="mb-3" controlId="formGridAddress1">
            <Form.Label>Address</Form.Label>
            <Form.Control/>
          </Form.Group>

          <Row className="mb-3">
            <Form.Group as={Col} controlId="formGridCity">
              <Form.Label>City</Form.Label>
              <Form.Control />
            </Form.Group>

            <Form.Group as={Col} controlId="formGridState">
              <Form.Label>State</Form.Label>
              <Form.Control />
            </Form.Group>

            <Form.Group as={Col} controlId="formGridZip">
              <Form.Label>Zip</Form.Label>
              <Form.Control />
            </Form.Group>
          </Row>
          <Button variant="primary" type="submit">
            Submit
          </Button>
        </Form>
      </Modal.Body>
      <Modal.Footer>
        <Button onClick={props.onHide}>Close</Button>
      </Modal.Footer>
    </Modal>
  );
}

export default App;
